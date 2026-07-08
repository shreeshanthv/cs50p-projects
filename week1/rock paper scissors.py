user = input("rock, Papers, Scissors: ").lower()
print ("You chose:", user)

if user != "rock" and user != "paper" and user != "scissors":
    print("Invalid input!")
else:
    computer = "rock"
    print("Computer chose:", computer)

    if user == computer:
        print("it's a tie!")
    elif user == "rock" and computer == "scissors":
        print("You win!")
    elif user == "paper" and computer == "rock":
        print("You win")
    elif user == "scissors" and computer == "paper":
        print("You win")
    else:
        print("You lose!")
   