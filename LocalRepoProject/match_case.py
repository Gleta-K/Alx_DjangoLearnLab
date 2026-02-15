import random
secret_number = random.randint(1,10)
guess = int(input("I'm thinking of a number between 1 and 10. Can you guess it?" ))
match guess:
    case  secret_number:
            print("Congratulations, you guessed it!")
    case > secret_number:
            print("Oops, your guess is a bit high. Try again!")
    case _:
            print("Nope, your guess is a bit low. Give it another shot!")
    if 
        
