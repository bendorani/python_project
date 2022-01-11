class Student:
    def __init__(self,name,id):
        if type(name)!=str:
            raise TypeError("name must to be string")
        if type(id)!=int:
            raise TypeError("id must to be int")
        if id<=0:
            raise ValueError("id must be above 0")
        self.name=name
        self.id=id
        self.subjectgrade={}
    def add_grade(self,name,grade):
        if type(name) != str:
            raise TypeError("name must to be string")
        if type(grade) != int:
            raise TypeError("grade must to be int")
        if grade< 0 or grade>100:
            raise ValueError("grade must be between 0-100")
        self.subjectgrade.update({name:grade})
    def calc_factor(self,name,factor):
        if type(name) != str:
            raise TypeError("name must to be string")
        if type(factor) != int:
            raise TypeError("factor must to be int")
        if factor<0:
            raise ValueError("factor must be above 0")
        if self.subjectgrade=={}:
            raise ValueError("you must have grades in your list")
        for i in self.subjectgrade:
            if i==name:
                self.subjectgrade[i]=(self.subjectgrade[i]*factor)//100+self.subjectgrade[i]
            if self.subjectgrade[i]>100:
                self.subjectgrade[name]=100
    def average(self):
        if self.subjectgrade=={}:
            raise ValueError("you must have grades in your list")
        sum=0
        for i in self.subjectgrade:
            sum+=self.subjectgrade[i]
        return sum/len(self.subjectgrade)
    def __repr__(self):
        return f"name:{self.name},id:{self.id} subjects and grades:{self.subjectgrade}\n"
    def __eq__(self, other):
        if type(other)!=Student:
            raise TypeError("you must compare with another student")
        if self.id == other.id:
            return True
        else:
            return False

