class Circle:
    def __init__(self,radius):
        self.radius=radius
        self.pie=3.14
    def area(self):
        sum_area=(self.radius*self.radius*self.pie)
        return sum_area
    def circumference(self):
        sum_circ=(self.radius*self.pie*2)
        return sum_circ
radius=int(input("enter radius: "))
circle1=Circle(radius)
print(circle1.area())
print(circle1.circumference())