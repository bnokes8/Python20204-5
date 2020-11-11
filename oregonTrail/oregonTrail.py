# Oregon Trail by Abram and Brady
# 11/3/20
# title screen that shows creators and copyright

# Function for the main menu. will ask the user what they want to do.
def menu_options(options):
    index = 1
    for i in options:
        print(str.format("{}){}",index,i))
        index+=1
    while True:

        userChoice = input("Select an option.  ")
        if userChoice.isnumeric():
            userChoice = int(userChoice)
            if userChoice >= 1 and userChoice <= len(options):
                return userChoice
            else:
                print("Not a valid number. Try again.")
        else:
            print("Enter a number.")


# Have to keep the title screen at the bottom just above where we call it
def title_screen():
  print('''
  \nOregon Trail by Abram and Brady
  \nCopyright Volcano Enterprises 2020
  \n
#     # ####### #        #####     #    #     # ####### 
#     # #     # #       #     #   # #   ##    # #     # 
#     # #     # #       #        #   #  # #   # #     # 
#     # #     # #       #       #     # #  #  # #     # 
 #   #  #     # #       #       ####### #   # # #     # 
  # #   #     # #       #     # #     # #    ## #     # 
   #    ####### #######  #####  #     # #     # #######\n''')
  while True:
    userChoice = ["Travel the trail","Learn about the trail", "Quit"]
    choice = menu_options(userChoice)
    if choice == 1:
      break
    if choice == 2:
      learn()
    if choice == 3:
      quit()
  play()

# learn

def learn():
    pages = [
'''' ___                               _____          _ _ 
 / _ \ _ __ ___  __ _  ___  _ __   |_   _| __ __ _(_) |
| | | | '__/ _ \/ _` |/ _ \| '_ \    | || '__/ _` | | |
| |_| | | |  __/ (_| | (_) | | | |   | || | | (_| | | |
 \___/|_|  \___|\__, |\___/|_| |_|   |_||_|  \__,_|_|_|
                |___/          ''',
"\nTry taking a journey by covered wagon across 2000 miles of plains, rivers, and mountains. Try! On the plains, will you slosh your oxen through mud and water-filled ruts or will you plod through dust six inches deep?",
#second page
'''\nHow will you cross the rivers? If have money, you might take a ferry (if there is one).
Or, you can ford the river and hope oyu and your wagon aren't swallowed alive!''',
#third page
'''\nWhat about supplies? Well, if you're low on food you can hunt.
You might get a buffalo...
You might. And there are bears in the mountains.''',
#fourth page
'''\nAt the Dalles, you can try navigating the Columbia River, but if running the rapids with a makeshift raft makes you queasy,
better take the Barlow Road.''',
#fifth page
'''\nIf for some reason you don't survive -- your wagon burns, or thieves steal your oxen, or you run out of provisions, die of Covid-19,
don't give up! Try again... and again... and again utnil your name is up there with the pro's.''',
#sixth page (credits)
'''This game was re-made by:
	Abram and Brady''']

    
    for page in pages:
        print(page)
        input("\nPress enter to go to the next page")



def family_Setup(question):
  wagonLeader = get_good_name("What is your name?")
  fam_list = []
  low = 2
  high = 7
  fam_members = get_good_number(question,low,high)
  for i in range(fam_members):
      name = get_good_name("What is their name?: ")
      fam_list.append(name)
  return fam_list, wagonLeader

def play():
  money = 0
  prof = ""
  listOfProfs = ["Banker","Carpenter","Farmer","Learn the difference"]
  money,prof = char_creator(listOfProfs)
  print(money, prof)
  family_Setup("How many family members do you have?")
  shop(money)
  


def char_creator(options):
  while True:
    choice = menu_options(options)
    if choice == 1:
      money = 1600
      prof = "Banker"
      break
    if choice == 2:
      money = 800
      prof = "Carpenter"
      break
    if choice == 3:
      money = 400
      prof = "Farmer"
      break
    if choice == 4:
      print(#info on profs
'''\nTravelling to Oregon isn't easy!
But if you're a banker, you'll have more money for supplies
and services than a carpenter
or a farmer.
\nHowever, the harder you have
to try, the more points you
deserve! Therefore, the
farmer earns the greatest
number of points and the
banker earns the least.\n''')
    input("Press enter to go back to pick your profession")

  return money, prof
def get_good_name(question):
    while True:
        name = input(question)
        if name.isnumeric and len(name) <=1 :
            print("Invalid Name")
        else:
            return name
            break

# NEED TO FINISH FIXING THE ERRORS
def get_good_number(question,low,high):
    while True:
        number = input(question)
        if number.isnumeric() :
            number = int(number)
            if number >=low and number <= high:
                return number
        print ("not a good number")


def shop(money):
    ammo = 0
    food = 0
    oxen = 0
    clothes = 0
    parts = 0
    bill = 0
    items = ["Oxen","Food","Ammunition","Clothes","Wagon Parts","Check out"]
    spentOnItems = [0.00,0.00,0.00,0.00,0.00,bill]
    print("\nBefore leaving Independence you should buy Equipment and Supplies")
    print(str.format("\nYou have {} in cash to make this trip",money))
    print("\nRemember you can buy supplies along the way so you dont have to spend it all now")
    input("\nPress enter to continue")
    while True:
        spentOnItems[len(spentOnItems)-1]-bill
        print("Welcome to the Volcano General Store")
        print("Here is a list of things you can buy")
        print()
        print("===================================================")
        for i in range(len(items)):
            print(str.format("\t{}:     {:20}     ${:.2f}",i+1,items[i],spentOnItems[i]))
        print("===================================================")
        print(str.format("Total Bill so far:     ${:.2f}",bill))
        print(str.format("Total Funds available:     ${:.2f}",money-bill))
        #call the number function
        choice = get_good_number("What do you want to buy?: ",1,6)
        
        if choice == 1:#choice 1 is oxen 
            bill -= spentOnItems[0]
            oxen = 0
            spentOnItems[0] = 0.00
            print("""
            There are 2 oxen in a yoke;
            I recommend at least 3 yokes
            I charge $40 a yoke""")
            print(str.format("Total Bill so far:     ${:.2f}",bill))
            answer = get_good_number("How many do you want to buy?: ",1,5)
            cost = answer*40
            bill += cost
            oxen = answer * 2
            spentOnItems[0] = cost
            
        if choice == 2:#choice 2 is food
            bill -= spentOnItems[1]
            food = 0
            spentOnItems[1] = 0.00
            print("""
            I recommend that you take at least 200 pounds of food for each person in your family.
            You'll need flower, sugar, bacon, and coffee, my price is 20 cents a pound.""")
            print(str.format("Total Bill so far:     ${:.2f}",bill))
            answer = get_good_number("How many pounds do you want to buy?: ",100,2500)
            cost = answer*.20
            bill += cost
            food = answer
            spentOnItems[1] = cost
            
        if choice == 3:
            bill -= spentOnItems[2]
            ammo = 0
            spentOnItems[2] = 0.00
            print("""
            I sell ammunition in boxes of 20 bullets.
            Each box costs $2.00""")
            print(str.format("Total Bill so far:     ${:.2f}",bill))
            answer = get_good_number("How many boxes do you want to buy?: ",1,250)
            cost = answer*2
            bill += cost
            ammo = answer * 20
            spentOnItems[2] = cost
        if choice == 4:
            bill -= spentOnItems[3]
            clothes = 0
            spentOnItems[3] = 0.00
            print("""
            You'll need warm clothing in the mountains. I recommend taking at least 2 sets of clothes per person.
            Each set is $10.00.""")
            print(str.format("Total Bill so far:     ${:.2f}",bill))
            answer = get_good_number("How many sets do you want to buy?: ",1,15)
            cost = answer*10.00
            bill += cost
            clothes = answer * 2
            spentOnItems[3] = cost
        if choice == 5:
            pass
        if choice == 6:
            if bill < money:#checks to make sure they didnt over spend  
                money = money-bill
                print(str.format("Your total is ${}",bill))
                print(str.format("You bought {} Oxen, {}lbs of Food, {} Bullets, {} Clothes.",oxen,food,ammo,clothes))
                return oxen,food,ammo,clothes
            else:
                input("You've spent too much money, press enter to retry!")
                oxen = 0
                food = 0
                ammo = 0
                clothes = 0
                bill = 0
                cost = 0
                spentOnItems = [0.00,0.00,0.00,0.00,0.00,bill]
                













  
##main game  
title_screen()
