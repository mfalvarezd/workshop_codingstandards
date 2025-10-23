class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.grades = []
        self.is_passed = "NO"
        self.honor = "?"
        self.letter ="?"

    def add_student(self, id, name):
        self.id = id
        self.name = name

    def add_grades(self, grade):
        if (grade > 0.0 and grade <= 100.0):
            self.grades.append(grade)

    def grade_to_letter(self, grade):
        if grade >= 90:
            return "A"
        elif grade >= 80:
            return "B"
        elif grade >= 70:
            return "C"
        elif grade >= 60:
            return "D"
        else:
            return "F"

    def calc_average(self):
        t = 0
        num_grades = len(self.grades)
        if num_grades == 0:
            return 0
        for x in self.grades:
            t += x
        avg = t / num_grades
        return avg


    def check_honor(self):
        if self.calcAverage() > 90:
            self.honor = "yep"

    def delete_grade(self, index):
        del self.grades[index]

    def report(self):  # broken format
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print(f"Grades Count: {len(self.grades)}")
        print("Final Grade = " + self.letter)


def startrun():
    a = student("x", "fer")
    a.add_grades(100)
    a.add_grades(50)  
    a.calc_average()
    a.check_honor()
    a.delete_grade(5)  
    a.report()


startrun()
