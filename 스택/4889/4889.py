answer = []

while True:
    stack = []
    count = 0
    s = input()
    if '-' in s:
        break
    for i in range(len(s)):
        if not stack and s[i] == '}':
            count += 1
            stack.append('{')
        elif stack and s[i] == '}':
            stack.pop()
        else:
            stack.append(s[i])
    count += len(stack)//2
    answer.append(count)

for i in range(len(answer)):
    print(i+1, '. ', answer[i], sep='')