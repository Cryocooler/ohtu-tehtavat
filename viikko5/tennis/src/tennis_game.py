class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0


    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1


    def map_tennis_score(self,score):
        # tennis_scores = {
        #     0: 'Love-All',
        #     1: 'Fifteen-All',
        #     2: 'Thirty-All',
        #     3: 'Forty-All'
        #     }

        tennis_scores = {
            0: 'Love',
            1: 'Fifteen',
            2: 'Thirty',
            3: 'Forty'
            }


       


        if score not in list(tennis_scores.keys()):
            return "Deuce"
        else:
            return tennis_scores[score]

    def determine_adv_winner(self, points1, points2):
        pt_delta = abs(points1 - points2)
        pt_order = points1 > points2

        if pt_delta <2:
            if pt_order:
                return "Advantage player1"
            else:
                return "Advantage player2"

        if pt_delta >= 2:
            if pt_order:
                return "Win for player1"
            else:
                return "Win for player2"

        


    def get_score(self):
        score = ""
        temp_score = 0

        if self.m_score1 == self.m_score2:
            score = self.map_tennis_score(self.m_score1)

        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            score = self.determine_adv_winner(self.m_score1, self.m_score2)

        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.m_score1
                else:
                    score = score + "-"
                    temp_score = self.m_score2

                if temp_score == 0:
                    score = score + "Love"
                elif temp_score == 1:
                    score = score + "Fifteen"
                elif temp_score == 2:
                    score = score + "Thirty"
                elif temp_score == 3:
                    score = score + "Forty"

        return score
