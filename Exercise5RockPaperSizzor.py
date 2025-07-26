import random

# Computer chooses a random number from 1, 2, or 3
computer = random.choice([1, 2, 3])

# Ask the user to input their number



user = int(input(f"Enter your number (1 for rock , 2 for paper and 3 for scissor):-"))

print(f"Computer choice: {computer}")
print(f"Your choice: {user}")




rock = 1
paper = 2
scissor = 3

score=0
userwin=score+10



if computer == user:
    print("Match Draw")
elif (computer == rock and user == paper) or (computer == paper and user == scissor) or (computer == scissor and user == rock):
    print("You Wins and Computer Loses")
    print(f"Your Score is:{userwin}")
    

else:
    print("Computer Wins and You Loses")
    

