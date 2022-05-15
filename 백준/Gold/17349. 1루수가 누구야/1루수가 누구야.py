import sys

order = []
cnt = 0
result = []
false = []

players = [1,2,3,4,5,6,7,8,9]

for _ in range(9):
    a,b = map(int,sys.stdin.readline().split())
    order.append([a,b])

for i in range(9):
    non_first = []
    first = []
    
    if order[i][0] == 1:
        order[i][0] = 0
    else:
        order[i][0] = 1
    
    for j in range(9):
        if order[j][0] == 1 :
            first.append(order[j][1])
        else:
            non_first.append(order[j][1])
    
    for k in first:
        if len((set(first))) == 1 and k in set(first) and k not in set(non_first):
            result.append(k)
        else:
            false.append(k)
    if len(first) == 0:
        for index in range(1,10):
            if index not in set(non_first):
                result.append(index)
    if order[i][0] == 0:
        order[i][0] = 1
    else:
        order[i][0] = 0        


if len(set(result)) == 1:
    print(result[0])
elif len(set(false)) == 9:
    print(-1)
elif len(set(result)) == 0:
    ans = []
    for i in range(1,10):
        if i not in set(false):
            ans.append(i)
    if len(ans) == 1:
        print(ans[0])
    else:
        print(-1)
else:
    print(-1)
