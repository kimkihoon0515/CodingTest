import sys

s = sys.stdin.readline().strip()    

flag = False
word = ''
result = ''

for i in s:
    if flag == False:    
        if i == '<':
            flag = True
            word +=i
        elif i == ' ':
            word += i
            result += word
            word = ''
        else:
            word = i + word
    else:
        word +=i
        if i == '>':
            flag = False
            result += word
            word = ''
print(result+word)