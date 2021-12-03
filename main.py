#Number Guessing Game 

#importing modules
import random
from art import logo

#printing logo
print(logo)

#generating a random integer between 1 and 100
number = random.randint(1, 100)

#printing the welcome statements
print("Welcome to the Number Guessing Game!!!")
print("\nI am thinking of a number between 1 and 100")
print("Try to guess it :)")

#asking the player the difficulty level of the game
difficulty_level = input("Choose a difficulty level: 'easy' or 'hard': ").lower()

#initializing total chances/lives based on difficulty selected
if difficulty_level == "easy":
  chances = 10
else:
  chances = 5

#initializing a boolean variable to store the state of the game
game_end = False

#function to compare the random number and the number guessed by the player
def check_guess(guess, num):
  if guess < num:
    if num - guess < 10:
      print("Your guess is Low")
    else:
      print("Your guess is Too Low")

  elif guess > num:
    if guess - num < 10:
      print("Your guess is High")
    else:
      print("Your guess is Too High")
  
  else:
    print(f"Your guess was correct! The number was {num} :)")
    global game_end
    game_end = True


while chances > 0 and not game_end:
  #printing the number of chances remaining
  print(f"\nYou have {chances} chances remaining to guess the number...")

  #taking input the player's guess
  guess_num = int(input("Make a Guess: "))

  #comparing the random number and the number guessed by the player
  check_guess(guess_num, number)

  #decreasing total chances left by 1 after every iteration
  chances-=1

  if chances > 0 and not game_end:
    print("Guess again :(")
  

#printing out the ending statements
if chances == 0 and not game_end:
  print("\nYou run out of moves. You Lose :(")
  print(f"The correct number was {number}")
