from re import template


class Player:
    def __init__(self, name, nationality, team, goals, assists):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.team = team

    def __str__(self):
        return str(self.name)
        #self.team, self.goals, self.assists
