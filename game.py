# Create a rock paper scissors game in Python

# Player should be able to type r, p, or s
# Computer will pick r, p or s

# Game will print out the results and keep track of wins, losses and ties

# Type q to quit

# 1) Build a REPL
import random
choices = ['r', 'p', 's']
wins = 0
losses = 0
ties = 0

# LOOP
while True:
    # READ
    player_cmd = input("Choose your weapon: [r] Rock, [p] Paper, [s] Scissors or [q] Quit.")
    cpu_cmd = random.choice(choices)
    print(f'You chose: {player_cmd}')
    print(f'CPU chose: {cpu_cmd}')
    # EVALUATE
    # Computer picks r/p/s
    # Compare player cmd to cpu cmd
    if player_cmd == 'r':
        if cpu_cmd == 'r':
            print("You tie!")
            ties += 1
        elif cpu_cmd == 'p':
            print("Woops, you lost! :(")
            losses += 1
        elif cpu_cmd == 's':
            print("Congrats! You win! :D")
            wins += 1
    elif player_cmd == 'p':
        if cpu_cmd == 'r':
            print("Congrats! You win! :D")
            wins += 1
        elif cpu_cmd == 'p':
            print("You tie!")
            ties += 1
        elif cpu_cmd == 's':
            print("Woops, you lost! :(")
            losses += 1
    elif player_cmd == 's':
        if cpu_cmd == 'r':
            print("Woops, you lost! :(")
            losses += 1
        elif cpu_cmd == 'p':
            print("Congrats! You win! :D")
            wins += 1
        elif cpu_cmd == 's':
            print("You tie!")
            ties += 1
    elif player_cmd == 'q':
        print("Thanks for playing, See you next time fam :^)")
        break
    else:
        print("Unknown Command! Please choose [r], [p], [s], or [q].")
    # Update results based on win/loss/tie

    # PRINT results and score
    print(f'CPU chose: {cpu_cmd}')
    print(f'\nWins: {wins}, Losses: {losses}, Ties: {ties}\n')