import random

print("Welcome to the Game")

def get_user_choice():
    print("Enter your choice:")
    print("1.Rock")
    print("2.Paper")
    print("3.Scissors")
    user_choice = int(input("Select a number from 1, 2 or 3 : "))
    if user_choice in [1, 2, 3]:
        return user_choice
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
        return get_user_choice()

def comp_choice():
    computer_choice = random.randint(1, 3)
    return computer_choice

def get_winner(user_choice,computer_choice):
    if user_choice==computer_choice:
        return "It's a tie!"
    elif (user_choice==1 and computer_choice==3) or (user_choice==2 and computer_choice==1) or (user_choice==3 and computer_choice==2):
        return "You win!"
    else:
        return "Computer wins!"

def play():
    user_choice = get_user_choice()
    computer_choice = comp_choice()

    choices = {1:'Rock', 2:'Paper', 3:'Scissors'}

    print("You chose " + choices[user_choice])
    print("Computer chose " + choices[computer_choice])

    result = get_winner(user_choice, computer_choice)
    print(result)

play()


