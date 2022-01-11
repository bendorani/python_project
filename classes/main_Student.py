from Student import Student
name=input("enter name: ")
id=int(input("enter id: "))
grade=int(input("enter grade: "))
student1=Student(name,id,grade)
if student1.checkPass():
    print("pass")
else:
    print("failed")
factor=int(input("enter factor precent: "))
student1.updateGrade(factor)
student1.show()