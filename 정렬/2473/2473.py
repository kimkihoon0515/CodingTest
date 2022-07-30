import sys

n = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))

li.sort()
ans = sys.maxsize
answer = []

for i in range(n-2):
    start = i+1
    end = n-1
    while start<end:
        summary = li[i]+li[start]+li[end]
        if abs(summary) < ans:
            ans = abs(summary)
            answer = [li[i],li[start],li[end]]
        if summary <0:
            start +=1
        if summary > 0:
            end -=1
        else:
            break

print(answer[0],answer[1],answer[2])