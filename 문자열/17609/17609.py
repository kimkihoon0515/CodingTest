""" 시간초과 오류가 나옴. 반복문으로 검사하는 과정이 많아서 그런듯
import sys

t = int(sys.stdin.readline().strip())

def pel(s):
    for i in range(len(s)):
        result = 0
        if s[i] !=s[-(i+1)]:
            new = s.replace(s[i],'')
            if pelindrom(new) == 0:
                result += 1
                break
    if result == 1:
        return True
    return False


def pelindrom(s):
    if s[0:] == s[::-1]:
        return 0

for _ in range(t):
    s = sys.stdin.readline().strip()
    if pelindrom(s) == 0:
        print(0)
    else:
        if pel(s):
            print(1)
        else:
            print(2)
"""
import sys

t = int(sys.stdin.readline())

def second(s,left,right):
    while (left < right): 
        if (s[left] == s[right]): # 회문 검사 맞으면 왼쪽 오른쪽에서 하나씩 줄여가면서 검사한다.
            left += 1
            right -= 1
        else:
            return False
    return True

def first(s,left,right): # 유사회문인지 회문인지 둘다 아닌지 검사하는 과정
    while (left < right):
        if (s[left] == s[right]):
            left += 1
            right -= 1
        else: # 유사회문인지 아닌지 검사하는 과정
            check1 = second(s,left+1,right) # 왼쪽에서 하나 제거 
            check2 = second(s,left,right-1) # 오른쪽에서 하나 제거
            if (check1 or check2):
                return 1 # 유사회문
            else:
                return 2 # 둘다 아님
    return 0 # 회문

for _ in range(t):
    s = sys.stdin.readline().strip()
    left = 0
    right = len(s) - 1
    ans = first(s,left,right)
    print(ans)