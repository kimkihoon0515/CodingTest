import sys

s = sys.stdin.readline().strip()

def makeTable(tmp):
    k = len(tmp)
    table = [0]*k
    i = 0
    for j in range(1,k):
        while i > 0 and tmp[i]!=tmp[j]:
            i = table[i-1]
        if tmp[i] == tmp[j]:
            i += 1
            table[j] = i
    return max(table)

answer = 0
for i in range(len(s)):
    tmp = s[i:len(s)]
    answer = max(answer,makeTable(tmp))
    
print(answer)