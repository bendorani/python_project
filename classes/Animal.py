class Animal:
    def __init__(self, name):
        self.name = name
        self.level_hungry = 5
        self.level_energy = 5

    def __repr__(self):
        return f"name:{self.name},level hungry:{self.level_hungry}, level energy:{self.level_energy}"

    def eat(self, gram):
        hungry = gram // 50
        energy = gram // 100
        for i in range(hungry):
            self.level_hungry -= 1
            if self.level_hungry <= 0:
                self.level_hungry = 0
                print("the animal is no longer hungry, she did not finish to eat")
                break
        for i in range(energy):
            if self.level_hungry > 0:
                self.level_energy -= 1
            if self.level_energy < 0:
                self.level_energy = 0

    def play(self, time_playing):
        time = time_playing // 10
        for i in range(time):
            self.level_energy -= 2
            if self.level_energy > 0:
                self.level_hungry += 2
            if self.level_energy <= 0:
                self.level_energy = 0
                print("the game is finished, the animal is tired")
                break
            if self.level_hungry >= 10:
                self.level_hungry = 10

    def rest(self, time_rest):
        time2 = time_rest // 20
        time3 = time_rest // 30
        for i in range(time2):
            self.level_energy += 1
            if self.level_energy >= 10:
                self.level_energy = 10
                print("the animal finished resting and wants to play")
        for i in range(time3):
            self.level_hungry += 1
            if self.level_hungry >= 10:
                self.level_hungry = 10
                print("the animal finished resting and wants to eat")
