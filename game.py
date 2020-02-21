import random
choices = ['r', 'p', 's']
wins = 0
losses = 0
ties = 0

win_txt = "Congrats! You win! :D"
loss_txt = "Woops, you came close. Try again!"
tie_txt = "You tie!"

def eval_moves(player_move, cpu_move):
    winning_moves = {'r': 's', 's': 'p', 'p': 'r'}
    if (player_move == cpu_move):
        print(tie_txt)
        return 0
    elif winning_moves[player_move] == cpu_move:
        print(win_txt)
        return 1
    else:
        print(loss_txt)
        return -1

while True:
    player_cmd = input("Choose your weapon: [r] Rock, [p] Paper, [s] Scissors or [q] Quit.\n")
    cpu_cmd = random.choice(choices)
    print(f'CPU chose: {cpu_cmd}\n')

    if player_cmd in choices:
        results = eval_moves(player_cmd, cpu_cmd)
        if results == 0:
            ties += 1
        elif results == 1:
            wins += 1
        elif results == -1:
            losses += 1
    elif player_cmd == 'q':
        print("Thanks for playing, See you next time fam :^)")
        score_file = open('./score.txt', 'w')
        score_file.write(f'\nWins: {wins}, Losses: {losses}, Ties: {ties}')
        score_file.close()
        exit()
    else:
        print("Unknown Command! Please choose [r], [p], [s], or [q].")

    print(f'\nWins: {wins}, Losses: {losses}, Ties: {ties}\n------------------------------------------------------------------\n')