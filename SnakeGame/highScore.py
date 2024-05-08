class High_score:

    high_score = 0
    def update_highscore(self,score):
        if self.high_score < score:
            self.high_score = score
    def get_highscore(self):
        return self.high_score




