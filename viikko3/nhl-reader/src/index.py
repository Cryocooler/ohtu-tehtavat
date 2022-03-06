import requests
from playerreader import PlayerReader
from playerstats import PlayerStats
#from player import Player
from functools import reduce


# class PlayerReader:
#     def __init__(self,url):
#         self._url = url

#     def get_players(self):
#         response = requests.get(self._url).json()
#         #self.requests.get(self.url).json()
#         players = []
#         for player_dict in response:
#             player = Player( player_dict['name'],
#             player_dict['nationality'],
#             player_dict['team'],
#             player_dict['goals'],
#             player_dict['assists'])

#             players.append(player)
#         return players

#     def __str__(self):
#         return 0

# class PlayerStats:
#     def __init__(self,reader):
#         self._reader = reader

#     def top_scorers_by_nationality(self, nationality):
#         self._nationality = nationality
#         players =  self._reader.get_players()
#         players_by_nat = [player for player in players if player.nationality
#             == self._nationality]

#         return sorted(players_by_nat,
#             key = lambda player: player.goals + player.assists,
#             reverse= True)




def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"

    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)
    # response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    # players = []

    # for player_dict in response:
    #     player = Player(
    #         player_dict['name'],
    #         player_dict['nationality'],
    #         player_dict['team'],
    #         player_dict['goals'],
    #         player_dict['assists']
    #     )

    #     players.append(player)
    # #print(players)

    #print("Players from FIN: \n")

    # fin_players = [i for i in players if i.nationality == 'FIN']
    # fin_players = sorted(fin_players,
    # key = lambda player: player.goals + player.assists,
    #  reverse= True)

    # for player in fin_players:
    #     print(player)
        #print(f"{player.name} {player.team}  {player.goals} + {player.assists} = {player.goals + player.assists}")


    #print(list(filter(lambda x: x.nationality == 'FIN', players)))
    # for player in players:
    #     filter(player.nationality == 'FIN')
    #     print(f"{player.name} team {player.team} goals {player.goals} assists {player.assists}")

if __name__ == "__main__":
    main()