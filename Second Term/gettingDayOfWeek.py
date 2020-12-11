#Brady Nokes Getting day of week
#imports
import datetime


#Functions
def get_day_of_week(target):
    try:
        this_date = datetime.datetime.strptime(target,"%Y-%m-%d")
        day_of_week = this_date.strftime("%A")
        return day_of_week
    except:
        return "Invalid YYYY-MM_DD Date"


print(get_day_of_week("1776-07-04")) #US Declaration of Independence adopted
print(get_day_of_week("1918-11-11"))#World War I Armistice
print(get_day_of_week("3-16-2001")) #Invalid


myName = "Jill"
def say_your_name():
       yourName = "Bob"
       print(yourName)
       print(myName)
       return

say_your_name()
print(yourName)
