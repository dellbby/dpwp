'''
Delia Akbari
August 20, 2015
Reusable Library
DPWP
'''

class Grade(object):
    def __init__(self):
        self.__name = ''

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self):
        pass

    #create array to hold grade info
class
    #Grade point scale, return number for each grade
    @staticmethod
    def get_grades(grade1, grade2, grade3, grade4):
        if [grade1, grade2, grade3, grade4] == 'A' or [grade1, grade2, grade3, grade4] == 'a':
                [g1, g2, g3, g4] =4
        elif [grade1, grade2, grade3, grade4] == 'B' or [grade1, grade2, grade3, grade4] ==  'b':
                [g1, g2, g3, g4] =3
        elif [grade1, grade2, grade3, grade4] == 'C' or [grade1, grade2, grade3, grade4] == 'c':
                [g1, g2, g3, g4] =2
        elif [grade1, grade2, grade3, grade4] == 'D' or [grade1, grade2, grade3, grade4] == 'd':
                [g1, g2, g3, g4] =1
        elif [grade1, grade2, grade3, grade4] == 'F' or [grade1, grade2, grade3, grade4] == 'f':
                [g1, g2, g3, g4] =0
        else:
                return 'invalid grade'
        return g1, g2, g3, g4

    @staticmethod
    def calc_gpa(g1,g2,g3,g4):
        gpa = (g1 + g2 + g3 + g4)/4
        return gpa