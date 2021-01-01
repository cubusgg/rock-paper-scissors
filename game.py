import random


def rating_file(name):
    with open('rating.txt', 'r') as file:
        for line in file:
            user, points = line.split()
            if user == name:
                return points
        return 0


def game(points, option):
    if option == "":
        option = ['paper', 'scissors', 'rock']
    else:
        option = option.split(',')

    length = len(option)
    half = (length - 1) / 2

    while True:
        user_move = input()
        computer_move = random.choice(option)

        if user_move == '!exit':
            print('Bye!')
            break
        elif user_move == '!rating':
            print(f'Your rating: {points}')
            break
        elif user_move not in option:
            print('Invalid input')
        else:
            user_move_id = option.index(user_move)
            computer_move_id = option.index(computer_move)
            wins = []

            if user_move_id != computer_move_id:
                if user_move_id >= half:
                    wins += [i for i in range(user_move_id - int(half), user_move_id)]
                else:
                    start_point = half - user_move_id
                    if user_move_id - 1 >= 0:
                        wins += [i for i in range(0, user_move_id)]
                    wins += [i for i in range(length - int(start_point), length)]

                if computer_move_id in wins:
                    print(f'Well done. The computer chose {computer_move} and failed')
                    points += 100
                else:
                    print(f'Sorry, but the computer chose {computer_move}')

            else:
                print(f'There is a draw ({computer_move})')
                points += 50


def main():
    name = input('Enter your name: ')
    print(f'Hello, {name}')
    points = rating_file(name)
    option = input('Paste your tape of game: ')
    print("Okay, let's start")
    game(int(points), option)


main()
