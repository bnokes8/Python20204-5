## Brady Nokes 9/29/20
# Guess My Number 1.0

# picks a random number
import random

theNum = random.randint(1,10)
##print(theNum )

print("\tWelcome to 'Guess my number'!")
print("\nI'm Thinking of a number between 1 and 10.")
print("Try to guess it in 3 attempts. ")

winner = False

guess = int(input("Pick a Number between 1 and 10: "))

if winner == False :
    if guess == theNum :
        winner = True

    elif guess < theNum :
        print("Guess Higher")

    else :
        print("Guess Lower")




if winner == False :
    guess = int(input("Pick a Number between 1 and 10: "))
    if guess == theNum :
        winner = True

    elif guess < theNum :
        print("Guess Higher")

    else :
        print("Guess Lower")




if winner == False :
    guess = int(input("Pick a Number between 1 and 10: "))
    if guess == theNum :
        winner = True

    elif guess < theNum :
        pass

    else :
        pass


if winner == True :
    print("You Win")
else :
    print("You Lose")
print("End of Game")
