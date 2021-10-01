a = list(map(str,input()))
b = list(map(str,input()))

result = [[0] * (len(a)+1) for i in range(len(b)+1)]


for i in range(1,len(a)+1):

    for j in range(1,len(b)+1):
        if a[i-1] == b[j-1]:
            result[i][j] = result[i-1][j-1] + 1
        else:
            result[i][j] = max(result[i][j-1],result[i-1][j])
print(max(max(result)))