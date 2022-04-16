class Student:
    name = ""
    roll = None
    clas = None
    def __init__(self, std_roll, std_name, std_class):
        self.roll = std_roll
        self.name = std_name
        self.clas = std_class

class Exam(Student):
    totalSubjects = None
    subList = []
    std_marks = {}
    def __init__(self, std_roll, std_name, std_class, subs):
        super().__init__(std_roll, std_name, std_class)
        self.totalSubjects = subs
        for i in range(self.totalSubjects):
            subName = input(f"Enter Subject-{i+1} Name: ")
            self.subList.append(subName)
    def getMarks(self):
        self.std_marks.clear()
        for subject in self.subList:
            marks = int(input(f"Enter Marks obtained in {subject}: "))
            if marks < 0 or marks > 100:
                raise("\tERROR: Value Overflow!")
            else:
                self.std_marks.update({subject: marks})
        print("\tMarks successfully updated!")
            
class Result:
    exam = None
    gradeList = {"A": 90, "B": 75, "C": 60, "D": 45}
    def __init__(self, exam):
        self.exam = exam
    def __grading(self, marks):
        for grades in self.gradeList.keys():
            if marks >= self.gradeList.get(grades):
                return grades
        return "Fail"
    def show(self):
        if len(self.exam.std_marks) == self.exam.totalSubjects:
            print("\nResult")
            print(f"Student Name: {self.exam.name}\tRoll No.: {self.exam.roll}\n\t\t--Scores--")
            for subject in self.exam.std_marks.keys():
                print(f"{subject}:",
                        self.exam.std_marks.get(subject),
                    "Grade:",
                        self.__grading(self.exam.std_marks.get(subject))
                )
            print(f"--------------------\nTotal marks : {sum(self.exam.std_marks.values())}/{self.exam.totalSubjects*100}")
            print("Overall Grade :",
                    self.__grading(sum(self.exam.std_marks.values())/self.exam.totalSubjects))
        else:
            print("\tERROR: Invalid Transaction!")

if __name__ == "__main__":
        name = input("Enter Student Name: ").upper()
        roll = int(input("\t  Roll No.: "))
        clas = int(input("\t  Standard: "))
        subs = int(input("No.  of  Subjects : "))
        Exam = Exam(roll, name, clas, subs)
        Result = Result(Exam)
        Result.exam.getMarks()
        Result.show()
