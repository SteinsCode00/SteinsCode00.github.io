import random

pictures = ["crab", "shrimp", "fish", "gourd", "coin", "chicken"]

def crabgame():
    balance = input("Choose your starting balance: ")
    try:
        bank = int(balance)
        print("You are starting with:", balance + " dollars.")
    except ValueError:
        input("Invalid amount - Please choose a round amount: ")
        print("Your starting balance is: ", balance)

# Betting phase
    bet_1 = input("Choose how much you want to bet for your first hand: ")
    try:
        cash_1 = int(bet_1)
        print("You are betting:", bet_1 + " dollars.")
    except ValueError:
        input("Invalid amount - please bet a round amount: ")
        print("You are betting:", bet_1 + " dollars.")

    bet_2 = input("Choose how much you want to bet for your second hand: ")
    try:
        cash_2 = int(bet_2)
        print("You are betting:", bet_2 + " dollars.")
    except ValueError:
        input("Invalid amount - please bet a round amount: ")
        print("You are betting:", bet_2 + " dollars.")

    current_balance = bank - cash_1 - cash_2

    print("Your current balance is " + str(current_balance) + " dollars.")

# Choosing phase
    player_choice1 = input("Pick your first bet (crab, shrimp, fish, gourd, coin or chicken): ")

    while player_choice1 not in pictures:
        player_choice1 = input("Invalid choice, please enter one of the six choices: ")

    player_choice2 = input("Pick your second bet (crab, shrimp, fish, gourd, coin or chicken): ")

    while player_choice2 not in pictures:
        player_choice2 = input("Invalid choice, Please enter one of the six choices: ")

# 3 dice rolls
    diceroll = random.choices(pictures, k=3)

# Show results of the roll
    print(diceroll)

# First choice results
    if player_choice1 in diceroll:
        print("You won the first bet!")
        current_balance += cash_1*2
        print("You won {0} dollars on your first bet.".format(str(cash_1)))
    else:
        print("You lost the first bet!")
        print("You lost {0} dollars.".format(str(cash_1)))

# Second choice results
    if player_choice2 in diceroll:
        print("You won the second bet!")
        current_balance += cash_2 * 2
        print("You won " + str(cash_2) + " dollars on your second bet.")
    else:
        print("You lost the second bet!")
        print("You lost " + str(cash_2) + " dollars.")


# Double win event
    if player_choice1 == player_choice2 and player_choice1 and player_choice2 in diceroll:
        print("Wow you won a double!")

# current total
    print("Your new balance is: ", str(current_balance) + " dollars.")

crabgame()


