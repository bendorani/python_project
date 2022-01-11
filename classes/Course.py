from classes.Student import Student
class Course:
    def __init__(self,numcourse,namecourse,maxstudents):
        if type(numcourse)!=int:
            raise TypeError("id course must be int")
        if type(namecourse)!=str:
            raise TypeError("name must be string")
        if type(maxstudents)!=int:
            raise TypeError("max student must be int")
        if maxstudents<=0:
            maxstudents=10
        self.idcourse=numcourse
        self.nameofcourse=namecourse
        self.dicsubject={}
        self.liststud=[]
        self.maxincourse=maxstudents
    def __repr__(self):
        return f"name:{self.nameofcourse}, id course:{self.idcourse} max in course:{self.maxincourse}" \
               f"\nsubjects in course: {self.dicsubject}\n" \
               f"{self.liststud}"

    def add_student(self,student:Student):
        if type(student)!=Student:
            raise TypeError("add student must get student")
        if self.maxincourse>len(self.liststud) and student not in self.liststud:
            self.liststud.append(student)
            return True
        else:
            return False
    def add_factor(self,subject,factor):
        if type(subject) != str:
            raise TypeError("subject must to be string")
        if type(factor) != int:
            raise TypeError("factor must to be int")
        if factor<0:
            raise ValueError("factor must be above 0")
        if self.liststud == []:
            raise ValueError("you must have grades in your list")
        for i in self.liststud:
            i.calc_factor(subject,factor)

    def del_student(self,student:Student):
        if type(student) != Student:
            raise TypeError("del student must get student")
        if self.liststud==[]:
            raise ValueError("you must have students in list")
        if student in self.liststud:
            self.liststud.remove(student)
    def averages(self):
        if self.liststud==[]:
            raise ValueError("you must have students in list")
        list2=[]
        for i in self.liststud:
            list2.append(i.average())
        return list2
    def weak_student(self):
        if self.averages() == []:
            raise ValueError("you must have students in list")
        for i in self.averages():
            if i<0 or i>100:
                raise ValueError("Average cant be below 0 or above 100")
        listindex=[]
        lowestavg=min(self.averages())
        for i in range(len(self.averages())):
            if self.averages()[i]==lowestavg:
                listindex.append(i)

        return listindex





