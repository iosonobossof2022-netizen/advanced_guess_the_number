import random
pc_num = random.randint(1, 500)
user_num = None
guess_count = 0

def user_guess(user_num, choices):
    user_num = int(input("Enter your guess (1-500): "))
    while user_num < 1 or user_num > 500:
        print("Invalid choice. Please choose a number between 1 and 500.")
        user_num = int(input("Enter your guess (1-500): "))
    return user_num

def check_guess(user_num, pc_num, guess_count):
    guess_count += 1
    if guess_count <= 2:
        if user_num != pc_num:
            print("Sorry, that's not the correct number. Try again.")
        elif user_num == pc_num:
            print(f"Congratulations! You've guessed the number {pc_num} in {guess_count} tries.")
            exit("you won")
    elif guess_count == 3:
        print(f"Sorry, you've used all your attempts. The correct number was {pc_num}.")
        exit("you lost")
    else:
        print("something went wrong")
        exit("error")

    return guess_count