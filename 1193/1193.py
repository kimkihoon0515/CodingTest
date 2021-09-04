a = int(input())

n = 1
b = 0
c = 0

while True:
    if c ==0:
        c =c+b+n
    else:
        c = c+b
        b+=1
        print(c)
        if b %2 ==0:
            print("%d/%d" %(1,))
        else:
            print("%d/%d" %()) 
            if c > a:
                break