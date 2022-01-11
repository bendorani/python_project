from Animal import Animal

name = input("enter name: ")
animal1 = Animal(name)
num = int(input("enter number of activity: "))
while num != 0:
    if num == 1:
        gram = int(input("enter how much gram the animal eat: "))
        animal1.eat(gram)
        print(animal1)
        num = int(input("enter number of activity: "))
    elif num == 2:
        time_play = int(input("enter how many minuets the animal played: "))
        animal1.play(time_play)
        print(animal1)
        num = int(input("enter number of activity: "))
    elif num == 3:
        time_rest = int(input("enter how many minutes she rest: "))
        animal1.rest(time_rest)
        print(animal1)
        num = int(input("enter number of activity: "))
print("the game is over")
