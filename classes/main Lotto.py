from Lotto import Lotto
from random import randint
lotto1=Lotto()
lotto1.numbers_got()
count=0
for i in range(6):
    num = int(input("enter guess number: "))
    if 1<=num<=45:
        if lotto1.guss(num):
            count+=1
    else:
        print("you failed because wrong gueses")
        count=0
        break
print(f"you won {lotto1.prize_amount(count)}")
