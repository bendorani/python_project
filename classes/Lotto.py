from random import randint


class Lotto:

    def __init__(self):
        self.low = 1
        self.up = 45
        self.listnumber = self.number_to_list()
        self.maxwin = self.max_of_winning()

    def number_to_list(self):
        number = []
        for i in range(6):
            number.append(randint(self.low, self.up))
        return number

    def max_of_winning(self):
        max = int(input("enter max winning amount: "))
        return max

    def numbers_got(self):
        for i in self.listnumber:
            print(i, end=" ")
        print()

    def guss(self, num):
        if num in self.listnumber:
            return True
        else:
            return False

    def prize_amount(self, guessright):
        if guessright <= 1:
            return 0
        else:
            return (guessright * self.maxwin) // 6
