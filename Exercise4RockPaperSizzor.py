import random
# Rock Paper Sizzzor Rules
# '''  Snake , Water and Gun is a variation of the children's game "rock-paper-sizzor"
    #  where players use hand gestures to represents a snake , 
    #  water, gyn .The gun beats the snake , the water beates the gun and the snake drinks the water .
    #  Write a python program to create a Snake water Gun game in
    #  python using if-else statements.Do not create any fancy GUI.Use proper functions to check for win.'''



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
    

