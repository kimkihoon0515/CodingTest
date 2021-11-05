import sys

li = list(map(str,input()))

result = 0
for i in li:
    if int(i) == 0 or int(i) == 1 or result <=1:
        result +=int(i)
    else:
        result *=int(i)
print(result)