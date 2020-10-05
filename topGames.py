# Brady Nokes 9/5/20
# Top 25 Games, Books, and Movies Mixed Together, Lists and Loops
game1 = "Terraria - Game"
movie1 = "The Invisible Man - Movie"
game2 = "Among Us - Game"
game3 = "Castle Crashers - Game"
game4 = "Mario Party 8 - Game"
game5 = "Skate 3 - Game"
book1 = "Oracle Series Book 1 - Book"
game6 = "Mortal Kombat 11 - Game"
movie2 = "Black Panther - Movie"
book2 = "Oracle Series Book 2 - Book"
game7 = "Mario Brothers Wii -  Game"
game8 = "COD BO1 - Game"
game9 = "Rainbow Six Siege - Game"
game10 = "Rocket League - Game"
game11 = "Garrys Mod - Game"
game12 = "Subnautica - Game"
movie3 = "Avengers - Movie"
book3 = "Animal Farm - Book"
game13 = "GTAV - Game"
movie4 = "The Sorcerers Apprentice- Movie"
game14 = "Left 4 Dead 2 - Game"
game15 = "Karlson - Game"
game16 = "Far Cry 5 - Game"
game17 = "Halo Reach - Game"
game18 = "Rust - Game"
topGames = ["Rust", # 0 
            "Halo Reach", # 1
            "Far Cry 5", # 2
            "Karlson",
            "Left 4 Dead 2",
            "The Sorcerers Apprentice",
            "GTAV",
            "Animal Farm",
            "Avengers",
            "Subnautica",
            "Garrys Mod",
            "Rocket League",
            "Rainbow Six Siege",
            "COD BO1",
            "Mario Brothers Wii",
            "Oracle Series Book 2",
            "Black Panther",
            "Mortal Kombat 11",
            "Oracle Series Book 1",
            "Skate 3",
            "Mario Party 8",
            "Castle Crashers",
            "Among Us",
            "The Invisible Man", #23 or -2
            "Terraria", # 24 or -1
            ]


#topGames [24] = "The Opaque Man"
topGames.append("game 26")
topGames.remove (topGames[15])
print(len(topGames))
print(topGames[2:6]) #use a colon to get a part of the list to print


if topGames[0] != "Halo Reach"  :
    print("You Failed")
