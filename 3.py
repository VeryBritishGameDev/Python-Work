#print every number between 1000-10000, where sum of digits = 10 and multiplied into more then 20

def splitnum(x):
    listinnum = []
    listinnum.append(x%10)
    listinnum.append((x%100)//10)
    listinnum.append((x//100)%10)
    listinnum.append(x//1000)
    return list(reversed(listinnum))

def myformat(x):
    firstel = x[0]*1000
    secel = x[1]*100
    thirdel = x[2]*10
    fourel = x[3]
    return(firstel+secel+thirdel+fourel)

def multiplylist(x):
    p = 1
    for digit in x:
        p = p*digit
    return p

cnt = 0
for i in range(1000, 10000):
    x = splitnum(i)
    if sum(x) ==  10 and multiplylist(x) > 20:
        cnt = cnt+1
        print(myformat(x))

print(cnt)
