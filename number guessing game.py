import random
def num_guess() :
    
    num_to_guess = random.randint(1, 25)
    attempts = 0
    guessed = False

    print( " Welcome to the Number Guessing Game! ")
    print ( " I'm thinking of a number between 1 and 25.")

    while not guessed :
        try : 
            guess = int(input(" Enter your guess : "))
            attempts +=1

            if guess < num_to_guess:
                print( " Too low! ")
            elif guess > num_to_guess :
                print ( " Too high! " )
            else :
                print ( f" Congratulations! You guessed the number in {attempts} attempts. " )
                guessed = True
        except ValueError :
            print ( " Please enter a valid number. ")

num_guess()