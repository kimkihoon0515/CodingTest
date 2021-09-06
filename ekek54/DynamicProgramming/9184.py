import sys

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20,20,20)
    if a < b and b < c:
        if arr[a][b][c] != 0:
            return arr[a][b][c]
        arr[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return arr[a][b][c]
    else:
        if arr[a][b][c] != 0:
            return arr[a][b][c]
        arr[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return arr[a][b][c]

arr=[[[0 for i in range(21)] for j in range(21)]for k in range(21)]

while(1):
    input_list=list(map(int,sys.stdin.readline().split(' ')))
    if input_list.count(-1) == 3:
        break
    print("w("+str(input_list[0])+',',str(input_list[1])+',',str(input_list[2])+') = '+str(w(*input_list)))
