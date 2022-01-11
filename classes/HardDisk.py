class HardDisk:
    def __init__(self):
        self.overall_area=100
        self.taken_Area=0
        self.num_of_files=0
    def show(self):
        print(f"over all giga:{self.overall_area},taken area:{self.taken_Area},number of files in disk:{self.num_of_files}")
    def addFILE(self,size):
        if type(size)!=int:
            raise ValueError("invalid number, must be int")
        if self.taken_Area+size<=self.overall_area:
            self.taken_Area+=size
            self.num_of_files+=1
            return True
        else:
            return False
    def delFile(self,size):

        if type(size)!=int:
            raise TypeError("invalid number, must be int")
        if self.taken_Area-size>=0:
            self.taken_Area-=size
            self.num_of_files-=1
        else:
            self.taken_Area=0
            self.num_of_files-=1