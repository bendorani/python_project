open_file=open('data.txt','w')
open_file.write("my open file\n")
open_file.write("my second line\n")
open_file.close()
rfile=open('data.txt','r')
print(rfile.read())
rfile.close()
rfile=open('data.txt','r')
# print(rfile.read(16))
print(rfile.readline())
with open('data.txt','a+') as file:
    file.write("hello!!")
with open('data.txt',"r") as file:
    print(file.read())
file.close()
with open('data.txt','r+') as file:
    count=0
    while True:
        count+=1
        line=file.readline()
        if not line:
            break
    print(count-1)
with open('data.txt','r+') as file:
    count=0
    for i in file:
        words=i.split()
        for word in words:
            count+=1
    print(count)
