import random
def roll_dice():
    return random.randint(1, 6)
def roll():
    print("Welcome to the Dice Rolling Game!")
    while True:
        input("Press Enter to roll the dice...")
        dice_roll = roll_dice()
        
        print("You rolled:", dice_roll)
        if dice_roll == 6:
            print("Congratulations! You rolled a 6. You win!")
        else:
            print("Sorry, you didn't roll a 6. Try again!")
        play_again = input("Do you want to play again? (yes/no):").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break
roll()
