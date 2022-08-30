s=input()
answer=''
for x in s:
    if 'a'<=x and x<='z':
        x=ord(x)+13
        if x>122:
            x-=26
        answer+=chr(x)
    elif 'A'<=x and x<='Z':
        x=ord(x)+13
        if x>90:
            x-=26
        answer+=chr(x)
    else:
        answer+=x

print(answer)
