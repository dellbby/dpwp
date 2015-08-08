__author__ = 'Dellbby'

#3 Strings (Strings & Variables below created with raw_input to get input from)
fullname = raw_input ("Enter your Name: ")
food = raw_input ("Enter your favorite food: ")
age = raw_input ("Enter a number between 1 and 10: ")
color = raw_input ("Enter your favorite color: ")
princess = raw_input ("Enter a Disney Princess: ")

#Array
employees = ["Ken", "Tilly", "Lizzy"]

#Numbers
time = 3
gap = 2


#Function---------------------------------------------------------------------
def add(time,gap):
	hour = time + gap
	return hour
hour = add (3,2)


#Conditional Statements-----------------------------------------------------------------------------------------

if age > 5:
    result1 = "Oh, I apologize, she won't be able to ride on the Haunted mansion ride."
else:
    result1 = "Wonderful, she is old enough to sit on the ride."
#if age is less than 5...
if age > 5:
    result2 = "She won't be able to go on our Drop of Doom rollercoaster either. "
else:
    result2 = "She is old enough to go on our Drop of Doom rollercoaster. "



#Story!!!
story = '''
Hello {fullname}! My name is {employees[2]}, Welcome to Disneyland Theme Park.
Here you will find several activities, fun rides, and amazing food.
First let us start with what you will be eating today.
I see your favorite food is {food}, great! You can find {food} in our food court right next to Toon Town.
At {time}PM, {princess} will come out for pictures, so you will be able to catch her in Toon Town as well.
You will have a {gap} hour gap where you can visit some of our new tours.
We have a few new employees that will be giving tours in our new Harry Potter themed maze. Be sure to talk
to {employees[0]} if you would like to sign up for the tour because tickets sell out quick!
After seeing Princess {princess}, around {hour}PM, I suggest going to the haunted mansion ride.
I see here your younger sibling is {age} years old. {result1} I also want to let you know that {result2}
'''
print story.format(**locals())
