import sys

n,l = map(int,sys.stdin.readline().split()) # 테이프 길이 L

li = sorted(list(map(int,sys.stdin.readline().split()))) # 오름차순 정렬

cnt = 1

tape = [li[0]-0.5,li[0]+l-0.5] # 테이프를 가장 첫 구멍을 막는데에다 쓰므로 그 범위를 먼저 구한다.

for i in range(1,len(li)):
    if tape[0]<=li[i]-0.5 and li[i]+0.5<=tape[1]: # 2번째 구멍부터는 테이프 범위 안에 있다면 넘기고 없으면 새롭게 테이프를 쓰는 방식으로 구현
        continue
    else:
        tape = [li[i]-0.5,li[i]+l-0.5]
        cnt +=1
print(cnt)
    
