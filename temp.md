# HiFi DSP SDK: Steps Followed and Errors Encountered

This document summarizes the steps we followed to run sample audio encoding/decoding algorithms using the DSP SDK Developer Guide, along with the errors we encountered while integrating ML models.

---

## 1. Running Sample Audio Algorithms

We strictly followed the steps provided in the **DSP SDK Developer Guide** to run the sample audio encoding/decoding algorithms and generate the final executable.  

- The executable was successfully built on our **simulator**.  
- When this executable was deployed and run on the **Orion O6 board**, it executed as expected without any errors.

---

## 2. Integrating ML Models

We then attempted to run machine learning models using the **XAF library** with **TFLM**.

- **Model used:**  The *person_detect_int8* example provided by Cadence.  
- **Toolchains used:** CIX DSP SDK toolchain (for hardware) and RI-2022.9 toolchain (for simulator).  

<!-- standalone - actual core name -->

### 2.1 Compilation on simulator with *hifi5_ss_sphpfpu_nn_dm128*  core:
- **Core configuration:** `hifi5_ss_sphpfpu_nn_dm128`  
- **Compilation Command used:**  

`python3 ./Scripts/xnnc.py --tflm --test_app xaf_tflm --build hifi --host_os 0`  

- **Run Command used:**  

`xt-run --mem_model /home/mcw/xtensa/XNNC/TFLM/build/xa_xaf_person_detect_int8_test -infile: test/test_inp/person_detect_int8_inp_list.txt`  

#### Error Encountered:
`Audio device closed main c[0] err:0`  

**There is no proper guide** for running XAF with *hifi5_ss_sphpfpu_nn_dm128* core.

---

### 2.2 Compilation on simulator with *NNE110_HiFi5_MAX* and HiFi + Neo Cores:

To work around the issue, we compiled the same model using the ***NNE110_HiFi5_MAX*** with NNE configuration.

- **Cores used:** `NNE110_HiFi5_MAX` & `HiFi + Neo`  
- **Compilation Command used:**  

`python3 ./Scripts/xnnc.py --tflm --test_app xaf_tflm --build nne`  

- **Run Command used:**  

`xtsc-run --define=SIMSCRIPT_FILE=../utils/dsp_sim.vec--define=TARGET_BIN= /home/mcw/xtensa/XNNC/TFLM/build/xa_xaf_person_detect_int8_test --define=TARGET_ARGS=-infile:../test/test_inp/person_data.raw -i=/home/mcw/xtensa/Xplorer-11.1.5-workspaces /install/builds/RI-2022.9-linux/NNE110_HiFi5_MAX/examples/XTSC/NNE.testbench/system.inc`  



When attempting to run the executable on the **simulator**, we encountered a **timeout error**.  
#### Error Encountered:
`Audio device ready.  
xaf_comp_get_status failed, Error code : -6 (message queue Timeout at xaf-tflite-person-detect-test.c:355)`  

- **Reason:** The IPC return calls from XAF were waiting for **physical hardware**, which is not present on the local machine.

### 2.3 Deploying the Executables to O6 Board:

We deployed the generated executables (built with **both core configurations** and using **toolchain: CIX DSP SDK**) onto the **Orion O6 board**, which contains the required hardware.   

#### Error Encountered:
 Executable format unsupported  

`
[error] - expected format: AARCH64, obtained format: Tensilica`  

---

## Summary

1. The example audio algorithms given in the CIX DSP SDK ran successfully on both simulator and Orion O6 board.  
2. ML model compilation fails on *hifi5_ss_sphpfpu_nn_dm128* core (missing documentation for XAF).  
3. Compilation succeeds with *NNE110_HiFi5_MAX* core, but running on the simulator fails due to hardware-dependent IPC calls.  
4. Deploying the executables (built with both configurations and both toolchains) to actual hardware (O6 board) fails due to an **executable format mismatch**.  
