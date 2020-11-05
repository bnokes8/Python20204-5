# Oregon Trail by Abram and Brady
# 11/3/20
# title screen that shows creators and copyright

# Function for the main menu. will ask the user what they want to do. 
def main_menu():
  #have to add some nice ascii for the main menu
  print('''\nWelcome to Oregon Trail
  
  \nWhat would you like to do?:
  \n1) Travel the Trail
  \n2) Learn about the Trail
  \n3) Quit the game''')
  while True:
    mainMenu = input("\nWhich number?: ")
    #if mainMenu in range(1,4) and type(mainMenu) == int:
    if "1" in mainMenu:
      #stuff for starting the game
      print("Playing Game")
      break
    elif "2" in mainMenu:
      # stuff for learning about the trail
      print ("The Oregon Trail was a 2,170-mile (3,490 km)[1] east-west, large-wheeled wagon route and emigrant trail in the United States that connected the Missouri River to valleys in Oregon. The eastern part of the Oregon Trail spanned part of what is now the state of Kansas and nearly all of what are now the states of Nebraska and Wyoming. The western half of the trail spanned most of the current states of Idaho and Oregon. You now get to attempt a simulation of this journey, going through every problem those people wouldve gone through yourself.")     
    elif "3" in mainMenu:
      #quit game
      print("But why quit the game, you have not played it yet")
      break
    else:
      print("That is not recognized, try again.")
    #else:
      #print("Not recognized, try again. Option 1, 2, or 3?")
    
  #if statement will go here


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
   #    ####### #######  #####  #     # #     # #######''')
  main_menu()

title_screen()
