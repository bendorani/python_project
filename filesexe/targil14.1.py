open_file=open('story.txt','w')
open_file.writelines("A boy is playing there.\nThere is a playground.\nAn airplane is in the sky.\nthe sky is pink.\nAlphabet and numbers are aloowed in the password")
open_file.close()
open_file=open('story.txt','r')
print(open_file.read().strip())
print("============================================")
with open('story.txt','r') as file:
    count=0
    for line in file:
        if line[0]!="t" and line[0]!="T":
            count+=1
file.close()
print(count)
with open('story.txt','r')as file:
    count=0
    for line in file:
        words=line.split()
        for i in words:
            if i=="the" or i=="The":
                count+=1
file.close()
print(count)
with open('story.txt','r') as file:
    count=0
    for line in file:
        words=line.split()
        for i in words:
            count+=1
    file.close()
print(count)
