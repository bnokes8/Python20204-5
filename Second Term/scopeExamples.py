import datetime

def get_day_of_the_week(target):
     try:
         thisDate = datetime.datetime.strptime(target,"%Y-%m-%d")
         dayOfWeek = thisDate.strftime("%A")
         return dayOfWeek
     except:
         "invalid YYYY-MM-DD date"
userInput = input("What is the date you want? YYYY-MM-DD ")
print(get_day_of_the_week(userInput))
