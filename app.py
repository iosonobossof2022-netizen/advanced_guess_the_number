import funct

print("GUESS THE NUMBER ADVANCED")

for i in range(3):
    funct.user_num = funct.user_guess(funct.user_num, funct.choices)
    funct.guess_count = funct.check_guess(
        funct.user_num, funct.pc_num, funct.guess_count
    )
    if funct.user_num == funct.pc_num:
        break
