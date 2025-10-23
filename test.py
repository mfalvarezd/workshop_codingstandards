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
        

    def calcAverage(self):
        t = 0
        num_grades = len(self.grades)
        if num_grades == 0:
            return 0
        for x in self.gradez:
            t += x
        avg = t / num_grades
        return avg


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
    a.addGrades(50)
    a.calcAverage()
    a.checkHonor()
    a.deleteGrade(5)  # IndexError
    a.report()


startrun()
