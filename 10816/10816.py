import sys

n = int(sys.stdin.readline())
a = list(map(int,sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int,sys.stdin.readline().split()))
hashmap = {} # 해시맵 방식으로 구현한다.
for i in a: # a의 원소들의 각각의 개수를 hashmap에 저장한다.
    if i in hashmap:
        hashmap[i] +=1
    else:
        hashmap[i] =1

print(' '.join(str(hashmap[i]) if i in hashmap else '0' for i in b)) #hashmap에서 b를 하나씩 확인하면서 출력한다. 개수가 있으면 출력하고 없으면 0으로