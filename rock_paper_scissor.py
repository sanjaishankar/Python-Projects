import random

user_wins = 0
computer_wins = 0
exit = False

while exit == False:
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose rock, paper, or scissors or exit: ")
    computer_input = random.choice(options)

    if user_input == "quit":
        print("Goodbye!")
        print("You Won a total score of " + str(user_wins) + " and the computer total score is " + str(computer_wins))
        exit = True

    if user_input == "rock":
        if computer_input == "rock":
            print("Your input: rock ")
            print("Computer input: rock")
            print("It's a Tie")
        elif computer_input == "paper":
            print("Your input: rock")
            print("Computer input: paper")
            print("Computer Wins!")
            computer_wins += 1

        elif computer_input == "scissors":
            print("Your input: rock ")
            print("Computer input: scissors")
            print("You Win!")
            user_wins += 1

    elif user_input == "paper":
        if computer_input == "rock":
            print("Your input: paper ")
            print("Computer input: rock")
            print("You Win!")
            user_wins += 1
        elif computer_input == "scissors":
            print("Your input: paper ")
            print("Computer input: scissors")
            print("Computer Wins!")
            computer_wins += 1
        elif computer_input == "paper":
            print("Your input: paper ")
            print("Computer input: paper")
            print("It's a Tie!")

    elif user_input == "scissors":
        if computer_input == "rock":
            print("Your input: scissors ")
            print("Computer input: rock")
            print("Computer Wins!")
            computer_wins += 1
        elif computer_input == "scissors":
            print("Your input: scissors ")
            print("Computer input: scissors")
            print("It's a Tie!")
        elif computer_input == "paper":
            print("Your input: scissors ")
            print("Computer input: paper")
            print("You Wins!")
            user_wins += 1
    elif user_input != "rock" or  user_input != "paper" or  user_input != "scissors":
        print("Invalid Input!!")






