import random

dificulties = {1 : 5, 2 : 10, 3 : 25, 4 : 50, 5 : 100}
rewards = {1 : 1, 2 : 2, 3 : 5, 4 : 10, 5 : 25}
variables = {
    "guess_coin" : 0,
    "user_num" : None,
    "guess_price" : 1,
    "difficulty" : 1,
    "guesses" : 3,
    "pc_num" : 0,
    "play_again" : None,
    "guessed" : False,
    }
variables["guess_reward"] = rewards[variables["difficulty"]]
variables["max_number"] = dificulties[variables["difficulty"]]


def pc_numf(variables):
    variables["pc_num"] = random.randint(1, variables["max_number"])

def user_guess(variables):
    variables["user_num"] = input(f"Enter your guess (1-{variables['max_number']}): ")

    while not variables["user_num"].isdigit() or int(variables["user_num"]) < 1 or int(variables["user_num"]) > variables["max_number"]:
        print("Invalid input. Please enter a number.")
        variables["user_num"] = input(f"Enter your guess (1-{variables['max_number']}: ")

    variables["user_num"] = int(variables["user_num"])

def buy_more_guesses(variables):
    while True:
        variables["buy_more"] = input(f"Would you like to buy more guesses for {variables['guess_price']} guess coins? (y/n): ")
        if variables["buy_more"].lower() == "y":
            if variables["guess_coin"] >= variables["guess_price"]:
                variables["guess_coin"] -= variables["guess_price"]
                variables["guess_price"] += 1
                variables["guesses"] += 1
                print(f"You have {variables['guess_coin']} guess coins left.")
                return
            else:
                print(f"You don't have enough guess coins to buy more guesses!, The correct number was {variables['pc_num']}.")
                exit("Game over.")
        elif variables["buy_more"].lower() == "n":
            print(f"Game over. The correct number was {variables['pc_num']}.")
            return
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")


def check_guess(variables):
    if variables["guesses"] >= 1:
        if variables["user_num"] != variables["pc_num"]:
            variables["guesses"] -= 1
            if variables["guesses"] > 0:
                print("Sorry, that's not the correct number. Try again.")
            else:
                print(f"Sorry, you've used all your attempts.")
                print(f"You have {variables['guess_coin']} guess coins")
            return False

        else:
            print(f"Congratulations! You've guessed the number {variables['pc_num']}")
            variables["difficulty"] = min(variables["difficulty"] + 1, max(dificulties))
            variables["max_number"] = dificulties[variables["difficulty"]]
            variables["guess_coin"] += variables["guess_reward"]
            print(f"You've advanced to level {variables['difficulty']}. The new range is 1-{variables['max_number']}.")
            print(f"You have {variables['guess_coin']} guess coins")
            return True

    elif variables["guesses"] == 0:
        print(f"Sorry, you've used all your attempts.")
        print(f"You have {variables['guess_coin']} guess coins")

        return False
    else:
        print("something went wrong")
        exit("error")


def play_again(variables):
    while True:
        variables["play_again"] = input("Would you like to play again? (y/n): ")
        if variables["play_again"] == "y" or variables["play_again"] == "Y":
            variables["guesses"] = 3
            return True
        elif variables["play_again"] == "n" or variables["play_again"] == "N":
            print("Thanks for playing!")
            exit()
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")

def game(variables):
    pc_numf(variables)

    while True:
        user_guess(variables)
        variables["guessed"] = check_guess(variables)

        if variables["guessed"]:
            if play_again(variables):
                variables["guess_reward"] = rewards[variables["difficulty"]]
                pc_numf(variables)
                continue

        if variables["guesses"] == 0:
            buy_more_guesses(variables)
            if variables["guesses"] > 0:
                continue

            if play_again(variables):
                variables["guess_reward"] = rewards[variables["difficulty"]]
                pc_numf(variables)
                continue