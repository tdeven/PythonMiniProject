import random
import math

Lower = int(input("Enter Lower Bound:"))
Upper = int(input("Enter Upper Bound:"))

x = random.randint(Lower, Upper)
print("\n\tYou've only", round(math.log(Upper - Lower + 1, 2)), "chance to guess the integer\n")

count = 0

while count < math.log(Upper - Lower + 1, 2):
    count += 1

    guess = int(input("Guess a number:"))

    if x == guess:
        print("Congurations You dit it in", count, "try")
        break
    
    elif x > guess:
        print("You guessed to small!")

    elif x < guess:
        print("You guessed too high!")

if count >= math.log(Upper - Lower +1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter Luck Next Time!")
