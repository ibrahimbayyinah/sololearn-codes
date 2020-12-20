# Modified from Al Sweigart's: Automate The Boring Stuff With Python

import random

num = random.randint(1, 20)

print("Hello. What is your name?")
name = input()
print(f"Hello {name}. I'm thinking of a number between 1 and 20.\nTake a guess.")

guessed = False
i = 0

while not guessed:
  i += 1
  guess = int(input())
  if guess > num:
    print(f"Your guess is too high {name}.\nTake a guess.")
  elif guess < num:
    print(f"Your guess is too low {name}.\nTake a guess.")
  else:
    print(f"Good job {name}. You have guessed my number in {i} guesses.")
    guessed = True
