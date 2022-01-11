class Person:
    def __init__(self,name,age,num_of_child):
        self.name=name
        self.age=age
        self.num_of_child=num_of_child
    def show(self):
        print(f"name:{self.name}, age:{self.age}, number of children:{self.num_of_child}")
    def hasChildren(self):
        if self.num_of_child>0:
            return True
        else:
            return False
    def ageGroup(self):
        if 0<=self.age<=18:
            return "child"
        elif 19<=self.age<=60:
            return "adult"
        elif 120>=self.age>=61:
            return "senior"
        else:
            return "not valid"
name=input("enter name: ")
age=int(input("enter age: "))
number_of_child=int(input("enter number of children: "))
person1=Person(name,age,number_of_child)
person1.show()
if person1.hasChildren():
    print("person have children")
else:
    print("person dont have children")
print(person1.ageGroup())
