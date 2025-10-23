class student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.grades = []
        self.is_passed = "NO"
        self.honor = "?"

    def addGrades(self, grade):
        if(grade>0 and grade <= 100):
            self.grades.append(grade)
        

    def calcaverage(self):
        t = 0
        for x in self.gradez:
            t += x
        len_grades = len(self.grades)
        if (len_grades)>0:
            return t/len_grades
        return 0


    def checkHonor(self):
        if self.calcAverage() > 90:
            self.honor = "yep"

    def deleteGrade(self, index):
        del self.gradez[index]

    def report(self):  # broken format
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + len(self.gradez))
        print("Final Grade = " + self.letter)


def startrun():
    a = student("x", "")
    a.addGrades(100)
   # a.addGrades("Fifty")  # broken
    a.calcaverage()
    a.checkHonor()
    a.deleteGrade(5)  # IndexError
    a.report()


startrun()
