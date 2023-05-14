import random
from time import sleep


def main():
    game()


def game():
    correct_number = random.randint(0, 100)
    welcoming()
    attempts = 0
    while attempts <= 11:
        attempts += 1

        if attempts >= 11:
            print('You exceeded the 10 attempts')
            sleep(1)
            print('You lost!')
            break

        playerguess = input('Guess a number from 0 to 100: ')
        
        if not playerguess.isdigit():
            print('Invalid input. Please enter a valid number.')
            continue

        playerguess = int(playerguess)
        if playerguess < 0 or playerguess > 100:
            print('Number out of range. Please enter a number from 0 to 100.')
            continue

        if playerguess > correct_number:
            print('The correct number is lower.')
        elif playerguess < correct_number:
            print('The correct number is higher.')
        else:
            print(f'Congratulations! You guessed the correct number in {attempts} attempts.')
            break


def welcoming():
    print('Welcome to the Guess the Number game!')
    sleep(1)
    print('To win this game, you will have to guess the correct number in the range of (0, 100).')
    sleep(1)
    print('You have 10 attempts to guess the correct answer')
    sleep(1)
    print('Good Luck!')
    sleep(1)


main()
