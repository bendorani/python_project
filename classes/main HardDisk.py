from HardDisk import HardDisk
disk1=HardDisk()

for i in range(5):
    size = int(input("enter size of file in giga: "))
    if disk1.addFILE(size):
       print("file has been add")
    else:
        print("you dont have enough area, file didnt added")

size_todel=int(input("enter size of file to delete: "))
disk1.delFile(size_todel)
disk1.show()
