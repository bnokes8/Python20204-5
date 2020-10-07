# Brady Nokes 9/5/20
# Top 25 Games, Books, and Movies Mixed Together, Lists and Loops
import random
game1 = "Terraria - Game "
game2 = "The Invisible Man - Movie "
game3 = "Among Us - Game "
game4 = "Castle Crashers - Game "
game5 = "Mario Party 8 - Game "
game6 = "Skate 3 - Game "
game7 = "Oracle Series Book 1 - Book "
game8 = "Mortal Kombat 11 - Game "
game9 = "Black Panther - Movie "
game10 = "Oracle Series Book 2 - Book "
game11 = "Mario Brothers Wii -  Game "
game12 = "COD BO1 - Game "
game13 = "Rainbow Six Siege - Game "
game14 = "Rocket League - Game "
game15 = "Garrys Mod - Game "
game16 = "Subnautica - Game "
game17 = "Avengers - Movie "
game18 = "Animal Farm - Book "
game19 = "GTAV - Game "
game20 = "The Sorcerers Apprentice- Movie "
game21 = "Left 4 Dead 2 - Game "
game22 = "Karlson - Game "
game23 = "World Of Warcraft"
game24 = "Far Cry 4 - Game "
game25 = "Rust - Game "
##top_games = ["Rust", # 0 if you do a parenthesis instead of a bracket it is a tuple. Lists are mutable and a tuple is inmutable
##            "Halo Reach", # 1
##            "Far Cry 5", # 2
##            "Karlson",
##            "Left 4 Dead 2",
##            "The Sorcerers Apprentice",
##            "GTAV",
##            "Animal Farm",
##            "Avengers",
##            "Subnautica",
##            "Garrys Mod",
##            "Rocket League",
##            "Rainbow Six Siege",
##            "COD BO1",
##            "Mario Brothers Wii",
##            "Oracle Series Book 2",
##            "Black Panther",
##            "Mortal Kombat 11",
##            "Oracle Series Book 1",
##            "Skate 3",
##            "Mario Party 8",
##            "Castle Crashers",
##            "Among Us",
##            "The Invisible Man", #23 or -2
##            "Terraria", # 24 or -1
##            ]
topGames = [ game1,
                game2,
                game3,
                game4,
                game5,
                game6,
                game7,
                game8,
                game9,
                game10,
                game11,
                game12,
                game13,
                game14,
                game15,
                game16,
                game17,
                game18,
                game19,
                game20,
                game21,
                game22,
                game23,
                game24,
                game25
                ]
##name = "Brady"
##print(len(topGames))
##
##print(len(name))
##x=0
##while x != len(top_games) : # the while loop will run until the statement = false
##    print("looping",x)
##    x+=1
##print("TopGames")
##y = 0
##while True:
##    print(y,end = "")
##    y+=1000
##    if y > 1000000 :
##        break


#topGames [24] = "The Opaque Man"
##topGames.append("game 26")
##topGames.remove (topGames[15])
##print(len(topGames))
##print(topGames[2:6]) #use a colon to get a part of the list to print
##
##
##if topGames[0] != "Halo Reach"  :
##    print("You Failed")
highScores = [443, 950, 1000, 410, 875, 600, 550, 500, 395, 380]

##print(max(highScores))
##print(min(highScores))
##
##print(max(topGames))
##print(min(topGames))

topGames.append("World Of Warcraft")
topGames.sort()
topGames.reverse()
topGames.insert(0,"Zelda Link")
topGames.insert(6,"Zelda Link")
##print(topGames.count("Zelda Link"))
##print(topGames.count("World Of Warcraft"))

num = topGames.index("Zelda Link",True)
game = topGames.pop(int(num))
##print(game)
newList = topGames.copy()
topGames.clear()#will clear the list
##topGames.remove("Zelda Link")#will remove one element at a time
##print(topGames.count("Zelda Link"))



##numbers = []
##x = 0
##while x != 100 :
##    numbers.append(random.randint(1000,10000))
##    x+=1
##    
##print(numbers)
##numbers.sort()
##print(numbers)
##numbers.reverse ()
##print(numbers)
##print(topGames)
##print(newList)
##print(len(newList)
points = 0
if len(newList) >= 25 :
    points+=25
else :
    points -= 25

if not topGames :
    points += 10
else :
    points -= 10

if "World Of Warcraft" in newList :
    points += 10
else:
    points -= 10

if newList.count("Zelda Link") > 1 :
    points -= 5
else :
    points += 5

if newList.index ("Zelda Link") == 0:
    points += 25
else :
    points -=25

if newList.count ("World Of Warcraft") > 1:
    points += 25
else :
    points -= 25

for i in newList:
    if "Pokemon" in i or "pokemon" in i:
        points -= 100
    if "Halo" in i or "halo" in i:
            points -= 100
    if "Fortnite" in i or "fortnite" in i:
        points -= 1000000000000
    if "smash" in i or "Smash" in i:
        points -= 50


if points >= 90:
    print("A")
elif points >= 80:
    print("B")
elif points >= 70:
    print("C")
elif points >= 60:
    print("D")
else:
    print("F")

print(points,"Points")
