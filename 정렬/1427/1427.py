n = int(input()) # 입력값 n을 받는다.

list = [] # n을 str형으로 넣어서 하나씩 분리한다.
for i in str(n):
    list.append(i)
list.sort(reverse=True) # 역순으로 정렬한다.

print(''.join(list)) # 합쳐서 출력한다.