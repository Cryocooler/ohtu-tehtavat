

class PlayerStats:
    def __init__(self,reader):
        self._reader = reader

    def top_scorers_by_nationality(self, nationality):
        self._nationality = nationality
        players =  self._reader.get_players()
        players_by_nat = [player for player in players if player.nationality
            == self._nationality]

        return sorted(players_by_nat,
            key = lambda player: player.goals + player.assists,
            reverse= True)
