import random

guess_coin = 0
user_num = None
guess_price = 1
difficulty = 1
dificulties = {1 : 5, 2 : 10, 3 : 25, 4 : 50, 5 : 100}
guesses = 3
max_number = dificulties[difficulty]
pc_num = 0

def pc_numf(max_number, pc_num):
    pc_num = random.randint(1, max_number)
    return pc_num

def user_guess(user_num, max_number):
    user_num = input(f"Enter your guess (1-{max_number}): ")

    while not user_num.isdigit() or int(user_num) < 1 or int(user_num) > max_number:
        print("Invalid input. Please enter a number.")
        user_num = input(f"Enter your guess (1-{max_number}): ")

    user_num = int(user_num)
    return user_num

def buy_more_guesses(guess_coin, guess_price, guesses):
    while True:
        buy_more = input("Would you like to buy more guesses? (y/n): ")
        if buy_more.lower() == "y":
            if guess_coin >= guess_price:
                guess_coin -= guess_price
                guess_price += 1
                guesses += 1
                print(f"You have {guess_coin} guess coins left.")
                return guess_coin, guess_price, guesses
            else:
                print("You don't have enough guess coins to buy more guesses!")
                exit("Game over.")
        elif buy_more.lower() == "n":
            print("Game over.")
            return guess_coin, guess_price, guesses
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")


def check_guess(user_num, pc_num, difficulty, guesses, max_number, guess_coin, guess_price):
    if guesses >= 1:
        if user_num != pc_num:
            guesses -= 1
            if guesses > 0:
                print("Sorry, that's not the correct number. Try again.")
            return difficulty, guesses, max_number, guess_coin, guess_price, False

        else:
            print(f"Congratulations! You've guessed the number {pc_num}")
            difficulty += 1
            max_number = dificulties[difficulty]
            guess_coin += 1
            return difficulty, guesses, max_number, guess_coin, guess_price, True

    elif guesses == 0:
        print(f"Sorry, you've used all your attempts. The correct number was {pc_num}.")
        print(f"You have {guess_coin} guess coins")
        guess_coin, guess_price, guesses = buy_more_guesses(guess_coin, guess_price, guesses)

        return difficulty, guesses, max_number, guess_coin, guess_price, False
    else:
        print("something went wrong")
        exit("error")


def play_again(guesses, guess_coin):
    while True:
        play_again = input("Would you like to play again? (y/n): ")
        if play_again == "y" or play_again == "Y":
            guesses = 1
            guess_coin = 0
            return True, guesses, guess_coin
        elif play_again == "n" or play_again == "N":
            print("Thanks for playing!")
            exit()
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")

def game(pc_num, user_num, difficulty, guesses, max_number, guess_coin, guess_price):
    pc_num = pc_numf(max_number, pc_num)

    while True:
        if guesses == 0:
            difficulty, guesses, max_number, guess_coin, guess_price, guessed = check_guess(
                user_num, pc_num, difficulty, guesses, max_number, guess_coin, guess_price
            )
            if guesses == 0:
                break

        user_num = user_guess(user_num, max_number)

        difficulty, guesses, max_number, guess_coin, guess_price, guessed = check_guess(
            user_num, pc_num, difficulty, guesses, max_number, guess_coin, guess_price
        )

        if guessed:
            break
            
    play_again(guesses, guess_coin)
