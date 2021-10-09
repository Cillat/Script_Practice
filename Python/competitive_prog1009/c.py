num,game_round = map(int,input().split())

sum_num = num * 2

game_result = []
tmp = 0
tmp_str = []
tmp_play = 0


for i in range(sum_num):
    game_result.append(int(i+1))
    game_result.append(int(0))
    game_result.append(input())


for j in range(game_round):
    for k in range(num):
        if game_result[6*k+2][j] == "G" and game_result[6*k+5][j] == "C":
            game_result[6*k+1] += 1
        elif game_result[6*k+2][j] == "G" and game_result[6*k+5][j] == "P":
            game_result[6*k+4] += 1
        elif game_result[6*k+2][j] == "C" and game_result[6*k+5][j] == "P":
            game_result[6*k+1] += 1
        elif game_result[6*k+2][j] == "C" and game_result[6*k+5][j] == "G":
            game_result[6*k+4] += 1
        elif game_result[6*k+2][j] == "P" and game_result[6*k+5][j] == "G":
            game_result[6*k+1] += 1
        elif game_result[6*k+2][j] == "P" and game_result[6*k+5][j] == "C":
            game_result[6*k+4] += 1

    for l in range(sum_num):
        for m in range(l+1,sum_num): 
            if game_result[3*l+1] < game_result[3*m+1] or (game_result[3*l+1] == game_result[3*m+1] and game_result[3*l] > game_result[3*m]):
                tmp_play = game_result[3*m]
                tmp = game_result[3*m+1]
                tmp_str = game_result[3*m+2]
           
                game_result[3*m] = game_result[3*l]
                game_result[3*m+1] = game_result[3*l+1]
                game_result[3*m+2] = game_result[3*l+2]
                
                game_result[3*l] = tmp_play
                game_result[3*l+1] = tmp
                game_result[3*l+2] = tmp_str
             


for game_set in range(sum_num):
    print(int(game_result[3*game_set]))

