class Grades(object):
    def __init__(self):
    #Grade point scale, return number for each grade
    def scale(self):
        pass

    def GetGrades(grade1, grade2, grade3, grade4):
        if [grade1, grade2, grade3, grade4] == 'A' or [grade1, grade2, grade3, grade4] == 'a':
                [g1, g2, g3, g4] =4
        elif [grade1, grade2, grade3, grade4] == 'B' or [grade1, grade2, grade3, grade4] ==  'b':
                [g1, g2, g3, g4] =3
        elif [grade1, grade2, grade3, grade4] == 'C' or [grade1, grade2, grade3, grade4] == 'd':
                [g1, g2, g3, g4] =2
        elif [grade1, grade2, grade3, grade4] == 'D' or [grade1, grade2, grade3, grade4] == 'd':
                [g1, g2, g3, g4] =1
        elif [grade1, grade2, grade3, grade4] == 'F' or [grade1, grade2, grade3, grade4] == 'f':
                [g1, g2, g3, g4] =0
        else:
                return 'invalid grade'
        return g1, g2, g3, g4

    def CalcGPA(g1,g2,g3,g4):
    GPA = (g1,g2,g3,g4)/4
    return GPA

    def main(name, GPA):
    print "The GPA for", name,"is",GPA
    return 0

    if __name__ == '__main__':
    name, grade1, grade2, grade3, grade4 = GetName()
    grades = GetGrades([grade1, grade2, grade3, grade4])
    GPA = CalcGPA(grades)
    main(name, GPA)
