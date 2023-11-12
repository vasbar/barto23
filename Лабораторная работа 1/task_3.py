list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
cnt=len(list_players)
team1=list_players[0:int(cnt/2)]
team2=list_players[int(cnt/2):]
print(team1)
print(team2)