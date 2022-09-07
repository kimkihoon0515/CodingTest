import sys

k = int(sys.stdin.readline())

for j in range(k):
    li = list(map(int,sys.stdin.readline().split()))
    li = li[1:]
    li.sort(reverse=True)
    ans = -1
    for i in range(len(li)-1):
        summary = li[i]-li[i+1]
        ans = max(ans,summary)
    print('Class',j+1)
    print('Max',str(li[0])+',','Min',str(li[-1])+',','Largest gap',ans)