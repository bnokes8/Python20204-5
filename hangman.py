# Brady Nokes 9/10/20
# Hangman
# Computer picks random word
#If the player is wrong to guess, add a body part
#if cant guess word right, stickman gets hung.
#Good Luck
#imports
import random
#capitalize it so var cant change
HANGMAN = (
'''
----------
|          |
|
|
|
|
|
|
|
----------------
''',
'''
----------
|        |
|        O
|
|
|
|
|
|
----------------
''',
'''
----------
|        |
|        O
|       -+-
|        +
|
|
|
|
----------------
''',
'''
----------
|        |
|        O
|      /-+-
|        +
|
|
|
|
----------------
''',
'''
----------
|        |
|        O
|      /-+-\\
|        +
|
|
|
|
----------------
''',
'''
----------
|        |
|        O
|      /-+-\\
|        +
|      |    
|      |    
|
|
----------------
''',
'''
----------
|        |
|        O
|      /-+-\\
|        +
|      |    |
|      |    |
|
|
----------------
''',
'''
----------
|        |
|        O
|      /-+-\\
|        +
|      |    |
|      |    |
|   ---
|
----------------
''',
'''
----------
|        |
|        O
|      /-+-\\
|        +
|      |    |
|      |    |
|   ---   ---
|
----------------
''' )

MAX_WRONG = len(HANGMAN)-1
WORDS = ("STATEMENT","LOOP","IDLE","SYNTAX","VARIABLE","LIST","TUPLE","INDENT","FUNCTIONS","DEBUGGING")
word = random.choice(WORDS)
#assignment
#10 python related terms
#be sure to define terms in comments

wrong = 0
used = []
soFar = "-"*len(word)

print("Welcome to Hangman. Good Luck!")

while wrong < MAX_WRONG and soFar != word:
    print(HANGMAN[wrong])
    print("\nYou've used the following letters:\n",used)
    print("\nSo far, the word is:\n",soFar)

    guess = input("\n\nEnter Your Guess: ")
    guess = guess.upper()
    print(guess)

    while guess in used:
        print("You've already guessed the letter",guess)
        guess = input("\n\nEnter Your Guess: ")
        guess = guess.upper()

    used.append(guess)

    if guess in word:
        print("\nYes!",guess, "is in the word!")
        
        # create a new so_far to include guess in the correct location
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new+=guess
            else:
                new+=soFar[i]
        soFar = new

    else:
        print("\nSorry,",guess, "isn't in the word.")
        wrong+=1
        
if wrong == MAX_WRONG:
    print(HANGMAN[wrong])
    print("\nYou've been hung!")
else:
    print("\nYou guessed it!")
    print("\nThe word was",word)
    
input("\nClick enter to leave")
        


        



#option 1
##index = random.randint(0,len(WORDS)-1)
##word = WORDS[index]
##print(word)

##word = random.choice(WORDS)



##x = 0 testing purposes
##while x < len(HANGMAN): 
##    print(HANGMAN[x])
##    input()
##    x += 1






