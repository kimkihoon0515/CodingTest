import sys

k = int(sys.stdin.readline())

li = list(sys.stdin.readline().split())

a = ''
b = ''  
visited = [0 for i in range(10)] # 0~9까지의 숫자를 넣기 위해 10개의 visit 배열을 만듬

def check(i,j,k):
    if k == '<':
        return i<j
    else:
        return i>j

def answer(index,s):
    global a,b
    
    if index == k+1: # 맨 처음 나타나는 값이 최소, 맨 마지막에 저장되는 것이 최대
        if len(a) == 0:
            a = s
        else:
            b = s
        return
    for i in range(10): # 0 ~ 9 까지 숫자를 대입하기 위해 재쉬
        if visited[i] == 0:
            if index == 0 or check(s[-1],str(i),li[index-1]):
                visited[i] = 1
                answer(index+1,s+str(i))
                visited[i] = 0

answer(0,'')
print(b)
print(a)
    