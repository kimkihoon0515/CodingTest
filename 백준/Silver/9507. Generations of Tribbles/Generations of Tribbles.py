import sys

t = int(sys.stdin.readline())

for i in range(t):
    s = [1,1,2,4]
    n = int(sys.stdin.readline())   

    for j in range(4,n+1):
        s.append(s[j-1]+s[j-2]+s[j-3]+s[j-4])
    print(s[n])