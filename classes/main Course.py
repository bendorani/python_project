from Course import Course
from Student import Student
name=input("enter name course: ")
id=int(input("enter id course: "))
maxstud=int(input("enter max students in course: "))
course1=Course(id,name,maxstud)
course1.dicsubject={"math":"michal","chemestry":"gil","sport":"kiril"}
idstud=int(input("enter id student: "))
i=-1
while idstud!=0:
    namestud = input("enter student name: ")
    if Student(namestud,idstud) not in course1.liststud:
        course1.liststud.append(Student(namestud,idstud))
        i+=1
        for j in course1.dicsubject:
            grade=int(input(f"enter grade for {j}: "))
            course1.liststud[i].add_grade(j,grade)
    else:
        print("student already in list")
    if course1.add_student(Student(namestud,idstud)):
        idstud=int(input("enter id student: "))
    else:
        break
print(course1)
subject=input("enter subject you want to give factor: ")
factor=int(input("enter precentage in numbers of factor: "))
if subject in course1.dicsubject:
    course1.add_factor(subject,factor)
print(course1)
for i in course1.weak_student():
    course1.liststud.remove(course1.liststud[i])
print(course1)


