from re import template


class Player:
    def __init__(self, name, nationality, team, goals, assists):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.team = team

    def __str__(self):
        return f"{self.name:20} {self.team} {self.goals} + {self.assists} = {self.assists + self.goals}"
        #self.team, self.goals, self.assists
