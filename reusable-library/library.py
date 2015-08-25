'''
Delia Akbari
August 20, 2015
Reusable Library
DPWP
'''

class Grade(object): #DataObject
    def __init__(self):
        self.__name = ''
        self.age = '' #make sure age is not less than 16
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
        if a < 16:
            print "This GPA Calculator won't work for your grade!"
        else:
            self.__age = a







    #create array to hold grade info
class GetGrades(object):
    def __init__(self):
    #Grade point scale, return number for each grade
    @staticmethod
    def get_grades(g1, g2, g3, g4):
        if [g1, g2, g3, g4] == 'A' or [g1, g2, g3, g4] == 'a':
                [g1, g2, g3, g4] =4
        elif [g1, g2, g3, g4] == 'B' or [g1, g2, g3, g4] ==  'b':
                [g1, g2, g3, g4] =3
        elif [g1, g2, g3, g4] == 'C' or [g1, g2, g3, g4] == 'c':
                [g1, g2, g3, g4] =2
        elif [g1, g2, g3, g4] == 'D' or [g1, g2, g3, g4] == 'd':
                [g1, g2, g3, g4] =1
        elif [g1, g2, g3, g4] == 'F' or [gg1, g2, g3, g4] == 'f':
                [g1, g2, g3, g4] =0
        else:
                return 'invalid grade'
        return g1, g2, g3, g4

    @staticmethod
    def calc_gpa(g1,g2,g3,g4):
        gpa = (g1 + g2 + g3 + g4)/4
        return gpa