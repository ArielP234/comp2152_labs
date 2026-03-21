# Week 02 - Lab 02
# Rock, Paper, Scissors Game

# 1. Define the choices array
choices = ["Rock", "Paper", "Scissors"]

# 2. Get player input
playerChoice = input("Enter your choice (1=Rock, 2=Paper, 3=Scissors): ")

# 3. Convert to integer
playerChoice = int(playerChoice)

# 4. Error handling for player choice
if playerChoice < 1 or playerChoice > 3:
    print("Error: Choice must be between 1 and 3.")
else:
    # 5. Get computer's choice (simulated input)
    computerChoice = input("Enter computer's choice (1-3): ")
    computerChoice = int(computerChoice)

    # Validate computer choice
    if computerChoice < 1 or computerChoice > 3:
        print("Error: Choice must be between 1 and 3.")
    else:
        # 6. Array indexing (subtract 1 because arrays are 0-indexed)
        playerChoiceName = choices[playerChoice - 1]
        computerChoiceName = choices[computerChoice - 1]

        # 7. Print choices
        print("You chose:", playerChoiceName)
        print("Computer chose:", computerChoiceName)

        # 8. Determine the winner
        if playerChoice == computerChoice:
            print("It's a tie!")
        elif playerChoice == 1 and computerChoice == 3:
            print("Rock beats Scissors - You win!")
        elif playerChoice == 2 and computerChoice == 1:
            print("Paper beats Rock - You win!")
        elif playerChoice == 3 and computerChoice == 2:
            print("Scissors beats Paper - You win!")
        else:
            print("You lose!")

        # 9. String comparison
        if playerChoiceName != "Rock":
            print("You didn't pick the classic Rock...")