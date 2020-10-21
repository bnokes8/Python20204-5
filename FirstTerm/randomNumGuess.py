## Brady Nokes 9/29/20
# Guess My Number 1.0

# imports random number library
import random

# intro
print("\tWelcome to 'Guess my number'!")

question = input("What difficulty would you like, Easy, Medium, Or Hard?: ")
if  ("Ea" in question) or ("ea" in question) or (question == "Easy") :
    dif = 1
    maxRange = 10
    tries = 3
elif ("M" in question) or ("m" in question):
    dif = 2
    maxRange = 50
    tries = 5
else :
    dif = 3
    maxRange = 100
    tries = 10



theNum = random.randint(1,maxRange)
print(theNum )


print("\nI'm Thinking of a number between 1 and "+str(maxRange)+".")
print("Try to guess it in "+str(tries)+" attempts. ")

# boolean win condition
winner = False

# 1st guess
guess = int(input("Pick a Number between 1 and "+str(maxRange)+": "))


if guess == theNum :
    winner = True

elif guess < theNum :
    print("Guess Higher")

else :
    print("Guess Lower")



# guess 2
if winner == False :
    guess = int(input("Pick a Number between 1 and "+str(maxRange)+": "))
    if guess == theNum :
        winner = True

    elif guess < theNum :
        print("Guess Higher")

    else :
        print("Guess Lower")



#guess 3
if winner == False :
    if dif > 1:
        guess = int(input("Pick a Number between 1 and "+str(maxRange)+": "))
        if guess == theNum :
            winner = True

        elif guess < theNum :
            pass

        else :
            pass
# guess 4
if winner == False :
    if dif > 1:
        guess = int(input("Pick a Number between 1 and "+str(maxRange)+": "))
        if guess == theNum :
            winner = True

        elif guess < theNum :
            print("Guess Higher")

        else :
            print("Guess Lower")
### guess 5
if winner == False :
    if dif > 2:
        guess = int(input("Pick a Number between 1 and "+str(maxRange)+": "))
        if guess == theNum :
            winner = True

        elif guess < theNum :
            print("Guess Higher")

        else :
            print("Guess Lower")
# guess 6
if winner == False :
    if dif > 2:
        guess = int(input("Pick a Number between 1 and "+str(maxRange)+": "))
        if guess == theNum :
            winner = True

        elif guess < theNum :
            print("Guess Higher")

        else :
            print("Guess Lower")
# guess 7
if winner == False :
    if dif > 2:
        guess = int(input("Pick a Number between 1 and "+str(maxRange)+": "))
        if guess == theNum :
            winner = True

        elif guess < theNum :
            print("Guess Higher")

        else :
            print("Guess Lower")
# guess 8
if winner == False :
    if dif > 2:
        guess = int(input("Pick a Number between 1 and "+str(maxRange)+": "))
        if guess == theNum :
            winner = True

        elif guess < theNum :
            print("Guess Higher")

        else :
            print("Guess Lower")
# guess 9
if winner == False :
    if dif > 2:
        guess = int(input("Pick a Number between 1 and "+str(maxRange)+": "))
        if guess == theNum :
            winner = True

        elif guess < theNum :
            print("Guess Higher")

        else :
            print("Guess Lower")

#last guess
if winner == False :
    guess = int(input("Pick a Number between 1 and "+str(maxRange)+": "))
    if guess == theNum :
        winner = True

    elif guess < theNum :
        print("Guess Higher")

    else :
        print("Guess Lower")

# end condition
if winner == True :
    print("You Win")
else :
    print("You Lose")
print("End of Game")
