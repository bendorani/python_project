from Bus import Bus
seats=int(input("enter number of seats: "))
bus1=Bus()
bus1.constractor(seats)
num=int(input("enter numbr activity: "))
while num!=0:
    name=input("enter name passenger: ")
    if num==1:
        bus1.get_on(name)
        print(bus1)
        num = int(input("enter numbr activity: "))
    elif num==2:
        bus1.get_off(name)
        print(bus1)
        num = int(input("enter numbr activity: "))
