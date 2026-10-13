# Python Module for random number generator
import random

# Generate a random integer between 1 and 10 (inclusive)
random_number = random.randint(1, 10)

# Live counter 
lives = 5
# The list to store the user guesses in
previous_guesses = []

# While loop function, if lives is greater than 0 and or true, it will loop the entire code
while lives > 0 or True:

    # Starting line of code, where the loop starts
    print()
    user_guess = int(input("Enter a number between 1 - 10: "))
    
    # If the user guess is outside the range of 1 to 10, then the while loop will repeat until user guess is inside parameters
    while user_guess < 1 or user_guess > 10:
        print("Please enter a number between 1 and 10.")
        user_guess = int(input("Enter a number between 1 - 10: "))
        print("Previous guesses:", previous_guesses)
        print()

    # If the user guess is repeated, a while loop will make the user stuck inside the function until they answer a. different number, it will also print their previous attempts
    while user_guess in previous_guesses:  # Check if the guess has already been made
        print("You have already guessed that number. Please try a different number.")
        # print("You have lives ", lives, " left.")
        user_guess = int(input("Enter a number between 1 - 10: "))
        print("Previous guesses:", previous_guesses)
        print()
        
    # Function breaks the while loop if user guesses the randomly generated number correctly
    if user_guess == random_number:
        print()
        print()
        print("Congratulations! You guessed the correct number.")
        print("Previous guesses:", previous_guesses)
        print("You finished with", lives, "lives!")
        break

    # Else, the user will be redirected to give an input to try and guess the answer when they put an incorrect answer
    else:
        print()
        print("Incorrect guess. Try again.")
        previous_guesses.append(user_guess) # stores the answer the user gave in the "previous guess" list
        lives -= 1 # subtracts 1 life from the "lives variable"
        print("Previous guesses:", previous_guesses)
        
        print("You have", lives, "left.")

    # The last input they user gave will be printed, a hint will be given if the random number is greater or lesser than the random number 
    if previous_guesses[-1] > random_number: # if last number inputed in list is greater than random number
        print("The random number is lower!")
    elif previous_guesses [-1] < random_number: # Else, if last number inputed in list is lesser than random number
        print("The random number is higher!")
    else: # When the input the user gave is exactly what the random number is
        print()

    # If user runs out of lives, it will print the end game comments and reveal the random number
    if lives == 0:
        
        print()
        print("You ran out of tries!")
        print("The correct answer is", random_number)
        print()
        print("Game Over")
        break # breaks the entire while loop to end game

