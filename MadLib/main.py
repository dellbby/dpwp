__author__ = 'Dellbby'

#3 Strings (Strings & Variables below created with raw_input to get input from)
fullname = raw_input ("Enter your Name: ")
food = raw_input ("Enter your favorite food: ")
age = raw_input ("Enter your age: ")
color = raw_input ("Enter your favorite color: ")
princess = raw_input ("Enter a Disney Princess: ")

#Array
employees = ["Ken", "Tilly", "Lizzy"]
employees.append("Bob")

#Story!!!
story = '''
Hello {fullname}! My name is {employees[2]}, Welcome to Disneyland Theme Park.
Here you will find several activities, fun rides, and amazing food.
First let us start with what you will be eating today.
I see your favorite food is {food}, great! You can find {food} in our food court right next to Toon Town.
At 3:00PM, {princess} will come out for pictures, so you will be able to catch her in Toon Town as well.
We have a few new employees that will be giving tours in our new Harry Potter themed maze. Be sure to talk
to {employees[0]} if you would like to sign up for the tour because tickets sell out quick!
'''
print story.format(**locals())
