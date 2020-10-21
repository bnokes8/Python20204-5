# Brady Nokes 9/21/20
# Create a Mad Libs for userInput
# Source https://www.azlyrics.com/lyrics/justinbieber/baby.html

# takes input from user
name=input("Enter a Name: ")
verb=input("Enter a Verb: ")
verb2=input("Enter a Verb: ")
##verb3=input("Enter a Verb: ")
##verb4=input("Enter a Verb: ")
##verb5=input("Enter a Verb: ")
##adj=input("Enter an Adjective: ")
##adj2=input("Enter an Adjective: ")
##adj3=input("Enter an Adjective: ")
##adj4=input("Enter an Adjective: ")
randWord=input("Enter a Random Word: ")
noun=input("Enter a Noun: ")
noun2=input("Enter a Noun: ")
#noun3=input("Enter a Noun: ")
#noun4=input("Enter a Noun: ")
#noun5=input("Enter a Noun: ")
#number=input("Enter a Number: ")
#drink=input("Enter a Drink: ")
#bodyPart=input("Enter a Body Part: ")
item=input("Enter an Item: ")
#place=input("Enter a Place: ")
relationship=input("Enter a Relationship you can have with someone: ")
##direction=input("Enter a random Direction: ")
##bodyPart=input("Enter a random Body Part")

# this is formatting a string. you put the {} and it will put in the next part after the end of the string
#var="something else"
#result = str.format("the {} string {} are {}","testing",var,"test")
#print(result)


## places what the user wrote into the quote
madLib = str.format('''You know you love me, I know you care
Just shout {0}, and I'll be there
You are my love, you are my heart
And we will never ever ever be apart

Are we a {1}? {2}, quit playing.
We're just {3}, what are you {4}?
Said there's another and {5} right in my {6}
My first {7} broke my {8} for the first time
And I was like...''',randWord,item,name,relationship,verb,verb2,noun,relationship,noun2)
##
##''',name,''', baby, baby oooh
##Like baby, baby, baby nooo
##Like baby, baby, baby oooh
##I thought you'd always be ''',adj,'''
##
##
##
##Oh, for you I would have done whatever
##And I just can't believe we ain't together
##And I wanna play it ''',adj4,''', but I'm losin' you
##I'll buy you ''',item,''', I'll buy you any ring
##And I'm in pieces, ''',name,''' fix me
##And just shake me 'til you ''',verb3,''' me from this ''',adj2,''' ''',noun2,'''
##I'm going ''',direction,''', ''',direction,''', ''',direction,''', ''',direction,'''
##And I just can't believe my first love won't be ''',verb4,'''
##
##And I'm like
##Baby, baby, baby oooh
##Like baby, baby, baby nooo
##Like baby, baby, baby oooh
##I thought you'd always be ''',adj3,''' (mine)'''))
print(madLib)

