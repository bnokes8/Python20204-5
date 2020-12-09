# Trivia game that reads a plain text file
# Brady Nokes
# 12/3/20
test_file = "Brady Nokes.txt" # will need to change the file name to match the test that you are taking
#imports
import sys
from datetime import datetime


# functions
def open_file(file_name,mode):
    """ Open and returns a open file with the given permissions """
    try:
        file = open("assets/test_files/"+file_name,mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program\n", e)
        try:
            time = datetime.now()
            error_time = time.strftime("%m/%d/%y %H:%M:%S")
            file = open("assets/error_log/error_log.txt","a")
            file.write(str(e)+" "+str(error_time)+"\n")
            input("\n\nPress the enter key to exit.")
            sys.exit()
        except:
            sys.exit()
        


    return file

def get_name():
    """Gets a name from the user and logs it. makes sure it is good. start date and time for the test"""
    time = datetime.now()
    test_time = time.strftime("%m/%d %H:%M")
    while True:
        name = input("Enter your Name, must be First and Last: ")
        if len(name) >= 3 and " " in name:
            name = name.title()
            return name, test_time
        else :
            print("not a good Name")


def next_line(file):
    try:
        line = file.readline()
        line = line.replace("/","\n")#put a / wherever you want the line to break and go onto a new line
        return line
    except:
        print("Something went wrong while reading a line from a file")
        sys.exit()



def question_block(file):
    category = next_line(file)
    question = next_line(file)
    choices = []
    for i in range(4):
        choices.append(next_line(file))

    correct = next_line(file)
    if correct:
        correct = correct[0]
    explanation = next_line(file)


    return category, question, choices, correct, explanation
    


    
def welcome(name,title,time):
    """welcome the player."""
    print("Welcome "+name+" to your MidTerm\n")
    print("Your test was created by "+title)
    print("Your test was started at "+time)


    
    


def main(test_file):
    score = 0
    totalQue = 0
    #get the name and test time from user
    name, time = get_name()
    # open file
    file = open_file(test_file,"r")
    # read the title from the file
    title = next_line(file)
    #start the test
    welcome(name,title,time)
    #get the first question
    category, question, choices, correct, explanation = question_block(file)
    #start the game loop
    while category:
        #add one to total questions every time we get a new question
        totalQue += 1
        print("\t\t",category,"\n")
        print(question)
        for i in range(len(choices)):
            print(str.format("\t{}:  {}",i+1,choices[i]))
        answer = input("What is your answer?: ")
        #check answer
        if answer == correct:
            print("\nRight!", end = " ")
            score += 1
        else:
            print("\nWrong.", end = " ")
        print(explanation)
        print("Score:",score, "\n\n")
        category, question, choices, correct, explanation = question_block(file)
    # close the file
    file.close()
    #finish up the game
    print("That was the last question!")
    print("You're final score is", score)
    print("Your report card was created at the following location")
    print("assets/report_cards/"+name+".txt")
    # create a report card for the user
    report_card(name,time,score,totalQue)
       

def report_card(name,time,score,totalQue):
    file_name = name
    try:
        file = open("assets/report_cards/"+file_name+".txt","w")
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program\n", e)
        try:
            time = datetime.now()
            error_time = time.strftime("%m/%d/%y %H:%M:%S")
            file = open("assets/error_log/error_log.txt","a")
            file.write(str(e)+" "+str(error_time)+"\n")
            input("\n\nPress the enter key to exit.")
            sys.exit()
        except:
            sys.exit
            
    file.write("\nName: "+name)
    file.write("\nTime test was started: "+str(time))
    file.write("\nScore: "+str(score))
    file.write("\nTotal Questions: "+str(totalQue))
    percentage = score/totalQue * 100
    if percentage >= 90:
        letter_grade = "A"
    elif percentage >= 80:
        letter_grade = "B"
    elif percentage >= 70:
        letter_grade = "C"
    elif percentage >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"
    time = datetime.now()
    end_time = time.strftime("%m/%d/%y %H:%M")
    file.write("\nPercent: "+str(percentage))
    file.write("\nLetter Grade: "+letter_grade)
    file.write("\nTest finished: "+end_time)

    file.close()
        


# main
main(test_file)
input()












