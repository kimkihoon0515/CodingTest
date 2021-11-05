import sys

s = input()
result = []

sum = 0
for i in s:
    if i.isalpha():
        result.append(i)
    else:
        sum +=int(i)

result.append(str(sum))
print(''.join(result))


