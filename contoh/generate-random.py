import random

f = open("data1.txt", "w")

n = 1
while n<10:
    f.write(str(random.randint(99,1200))+"\n")
    n+=1

f.close()