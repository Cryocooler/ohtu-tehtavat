import requests
from player import Player
from functools import reduce

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    response = requests.get(url).json()

    #print("JSON-muotoinen vastaus:")
    #print(response)

    players = []

    for player_dict in response:
        player = Player(
            player_dict['name'],
            player_dict['nationality'],
            player_dict['team'],
            player_dict['goals'],
            player_dict['assists']
        )

        players.append(player)
    #print(players)
    print("Players from FIN: \n")

    fin_players = [i for i in players if i.nationality == 'FIN']
    fin_players = sorted(fin_players, key = lambda player: player.goals + player.assists, reverse= True)
    for player in fin_players:
        print(player)
        #print(f"{player.name} {player.team}  {player.goals} + {player.assists} = {player.goals + player.assists}")
    

    #print(list(filter(lambda x: x.nationality == 'FIN', players)))
    # for player in players:
    #     filter(player.nationality == 'FIN')
    #     print(f"{player.name} team {player.team} goals {player.goals} assists {player.assists}")

if __name__ == "__main__":
    main()