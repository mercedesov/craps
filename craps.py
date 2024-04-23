import random


def play_craps():
    # First time throw
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    sum = dice1 + dice2
    print(f"The sum of dice is {dice1} + {dice2} = {sum}")

    # Checks the result
    if sum in (7, 11):
        print("You won")
    elif sum in (2, 3, 12):
        print("You lose")
    else:
        print(f"Now your goal number is {sum}")
        # Second throw if needed
        while True:
            dice11 = random.randint(1, 6)
            dice22 = random.randint(1, 6)
            new_sum = dice11 + dice22
            print(f"The sum of dice is {dice11} + {dice22} = {new_sum}")
            # Checks the result for second throw
            if new_sum == sum:
                print("You won")
                break
            elif new_sum == 7:
                print("You lose")
                break


# Throw dice
play_craps()
