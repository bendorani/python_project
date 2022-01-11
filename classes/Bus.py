class Bus:
    def __init__(self):
        self.listseats=[]
        self.people_in_bus=0
    def constractor(self,numseats):
        for i in range(numseats):
            self.listseats.append("free")
    def get_on(self,namepassenger):
        for i in range(len(self.listseats)):
            if self.listseats[i]=="free":
                self.listseats[i]=namepassenger
                self.people_in_bus+=1
                break
        else:
            print(f"bus is full, {namepassenger} didnt get on")
    def get_off(self,namepassenger):
        for i in range(len(self.listseats)-1):
            if namepassenger==self.listseats[i]:
                self.listseats[i]="free"
                self.people_in_bus-=1
            break
        print(f"{namepassenger} is not in bus")
    def __repr__(self):
        return f"{self.listseats}\n {self.people_in_bus} is the amount of people in bus"
