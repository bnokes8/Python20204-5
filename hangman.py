# Brady Nokes 9/10/20
# Hangman
# Computer picks random word
#If the player is wrong to guess, add a body part
#if cant guess word right, stickman gets hung.
#Good Luck
#imports
import random
#cap it so var cant change

HANGMAN = (
'''
----------
|         |
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
|       O
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
|       O
|      -+-
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
|       O
|     / -+-
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
|       O
|     / -+-\\
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
|       O
|     / -+-\\
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
|       O
|     / -+-\\
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
|       O
|     / -+-\\
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
|       O
|     / -+-\\
|        +
|      |    |
|      |    |
|   ---   ---
|
----------------
''' )

MAX_WRONG = len(HANGMAN)-1
WORDS = ("OVERUSED","CLAM","GUAM","TAFFETA","PYTHON")
word = random.choice(WORDS)
#assignment
#10 python related terms
#be sure to define terms in comments
wrong = 0
used = []
soFar = " _ "*len(word)

print("Welcome to Hangman. Good Luck!")
print()
print(HANGMAN[wrong])
print(soFar)



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









