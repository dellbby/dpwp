'''
Delia Akbari
August 20, 2015
Reusable Library
DPWP
'''

class Grade(object): #DataObject
    def __init__(self):
        self.__name = ''
        self.__age = '' #make sure age is not less than 16
        self.g1 = ''
        self.g2 = ''
        self.g3 = ''
        self.g4 =''

#GETTER AND SETTER FOR NAME:
    @property #getter for Name
    def name(self):
        pass

    @name.setter #Setter for Name
    def name(self, n):
        self.__name = n #signing parameter here

#GETTER AND SETTER FOR AGE:
    @property #getter for age
    def age(self):
        pass

    @age.setter
    def age(self, a):
        if a < 16: #checks to make sure student isn't younger than 16
            print "Error,This GPA Calculator won't work for your grade!"
        else:
            self.__age = a



    #create array to hold grade info
class GetGrades(object):
    def __init__(self):
    #Grade point scale, return number for each grade
        pass


    def calc_gpa(self, g):
        if g.g1 == 'A':
            grade1 = 4.0
        if g.g1 == 'B':
            grade1 = 3.0
        if g.g1 == 'C':
            grade1 = 2.0
        if g.g1 == 'D':
            grade1 = 1.0
        if g.g1 == 'F':
            grade1 = 0.0

        if g.g2 == 'A':
            grade2 = 4.0
        if g.g2 == 'B':
            grade2 = 3.0
        if g.g2 == 'C':
            grade2 = 2.0
        if g.g2 == 'D':
            grade2 = 1.0
        if g.g2 == 'F':
            grade2 = 0.0

        if g.g3 == 'A':
            grade3 = 4.0
        if g.g3 == 'B':
            grade3 = 3.0
        if g.g3 == 'C':
            grade3 = 2.0
        if g.g3 == 'D':
            grade3 = 1.0
        if g.g3 == 'F':
            grade3 = 0.0

        if g.g4 == 'A':
            grade4 = 4.0
        if g.g4 == 'B':
            grade4 = 3.0
        if g.g4 == 'C':
            grade4 = 2.0
        if g.g4 == 'D':
            grade4 = 1.0
        if g.g4 == 'F':
            grade4 = 0.0
        avg = (grade1 + grade2 + grade3 + grade4) / 4
        return avg