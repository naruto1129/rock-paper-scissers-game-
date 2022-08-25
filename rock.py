# We are importing random function
import random

# Printing the controls of the game
print("Hello Everyone Welcome To Our New Game")
print("Press 1 for rock")
print("Press 2 for paper")
print("Print 3 for scissors")

# To get the input from the user
user_choice = int(input())

# To check what option does the player chose 
if user_choice == 1:
    print("You have choosen rock")
if user_choice == 2:
    print("You have choosen paper")
if user_choice == 3:
    print("You have choosen scissors")

# A list to get input from computer
lst = [1, 2, 3]

computer_choice = random.choice(lst)

# It is the condition to check what computer chooses
if computer_choice == 1:
    print("Computer has choosen rock")
if computer_choice == 2:
    print("Computer has choosen paper")
if computer_choice == 3:
    print("Computer has choosen scissors")

# It is the condition to check that the both players wins the game 
if user_choice == 1 and computer_choice == 1:
    print("You both won")
if user_choice == 2 and computer_choice == 2:
    print("You both won")
if user_choice == 3 and computer_choice == 3:
    print("You both won")

#It is the condition to check that the player wins the game 
if user_choice == 1 and computer_choice == 3:
    print("You won")
if user_choice == 2 and computer_choice == 1:
    print("You won")
if user_choice == 3 and computer_choice == 2:
    print("You won")

#It is the condition to check that the computer wins the game
if user_choice == 1 and computer_choice == 2:
    print("You lose")
if user_choice == 2 and computer_choice == 3:
    print("You lose")
if user_choice == 3 and computer_choice == 1:
    print("You lose")

# Saluation for the game 
print("Thank You For Playing")

# And the game ends here 