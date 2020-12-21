# Modified from Al Sweigart's: Automate the Boring Stuff with Python

import random

num = random.randint(1, 20)


guess0 = input("Enter your guess: \n")
    
try:
    guess = int(guess0)
    
    if guess == num:
        print(f"Good job! You managed to guess the number, congratulations!")
    elif guess > 20 or guess < 1:
        print(f"You need to enter an integer between 1 and 20. Run the program another time and try again.")
    else:
        print(f"Nice try, but this is not the correct number. The correct number is in fact: {num}. But don't give up! Run the program another time and try again.")
        
except:
    print("Invalid input. Run the program another time and please make sure you enter an integer value between 1 and 20.")
