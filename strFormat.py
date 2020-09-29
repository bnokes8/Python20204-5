var = "something else"

# adding ":" in the {} will set however many spaces you want after it. you just put the number of spaces after the :
# after your spaces you can do a "." and it will cap the number of characters that the {} will use
# the ^ places the string in the center. if you add < or > after the ":" it will put however many spaces in whatever direction the arrow is pointing.
##result = str.format("the {0:>50} string {1:^50} are {2:<50}","123456789101112",var,"test2")
##print(result)
#this will put the number at the very left
print(str.format("Example 'd':{0:15d}",1500000))
# this will put commas in their respective places
print(str.format("Example ',':{0:15,}",1500000))
# this will put it in scientific notation
print(str.format("Example 'e':{0:15e}",3.14159))
#this will put them in percentages. putting the . after the 15 and adding 2 it will only put 2 zeros after the 75.
print(str.format("Example '%':{0:15.2%}",.75))
