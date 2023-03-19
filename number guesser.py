# My first basic number guessing game. Thank you to Tech with Tim YouTube Channel for lesson
# With the help of some Googling, I also wanted to add another element - a score for the user as well as a limted to guesses (5).
import random

# Prompt the user to enter a number for the top of range
while True:
    top_of_range = input("Enter a number to play!")
    if top_of_range.isdigit():
        top_of_range = int(top_of_range)
        if top_of_range <= 0:
            print("Please enter a number larger tan zero to have fun!")
        else:
            break

    else:
        print("Please enter a valid number")

# Now this section will all for the generation of a random number within the range

random_number = random.randint(1, top_of_range)

# User score. Variables for scoring and number of guesses.

score = 0
guesses_left = 5

# In this next section of the code will will begin the guessing loop
# The purpose of this is to also give the user basic hints until they guess the correct number
# I also wanted to add a choice for the player to play again if they wanted to regardless of outcome

print("Welcome to the game, I'm thinking of a number between 1 and", top_of_range)
while True:
    user_guess = input("What's your guess? ")
    if user_guess.isdigit():
       user_guess = int(user_guess)    
       if user_guess < 1 or user_guess > top_of_range:
           print("Your guess is incorrect. Try again")
       elif user_guess < random_number:
           print("Good try, but it's too low. Guess again!")
           guesses_left -= 1
       elif user_guess > random_number:
           print("Good try, but it's too high. Guess again!")
           guesses_left -= 1
       else:
           print("Congratulations! You're a guessing master")
           print("You guessed the number in", 5-guesses_left+1, "guesses.")
           score += guesses_left
           print("Your score is now", score)
           play_again = input("Don you want to play again? (y/n) ")
           if play_again.lower() == 'y':
               random_number = random.randint(1, top_of_range)
               guesses_left = 5
               print("Awesome, let's play again!")
           else:
                print("Thanks for playing! your finale score is", score)
           break

    else:
        print("Please enter a valid number")

    if guesses_left == 0:
        print("Sorry, you ran out of guesses. The number was", random_number)
        score -= 5
        print("You score now is", score)
        play_again = input("Don you want to play again? (y/n) ")
        if play_again.lower() == 'y':
               random_number = random.randint(1, top_of_range)
               guesses_left = 5
               print("Awesome, let's play again!")
        else:
            print("Thanks for playing! your finale score is", score)
                    

