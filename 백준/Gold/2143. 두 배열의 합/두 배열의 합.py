import bisect
T = int(input())
N = int(input())
Aarr = list(map(int,input().split()))
M = int(input())
Barr = list(map(int,input().split()))
Asum = []
Bsum = []
for i in range(N):  #O(A*(A-1)/2)
    s = Aarr[i]
    Asum.append(s)
    for j in range(i+1,N):
        s+=Aarr[j]
        Asum.append(s)
for i in range(M):  #O(B*(B-1)/2)
    s = Barr[i]
    Bsum.append(s)
    for j in range(i+1,M):
        s+=Barr[j]
        Bsum.append(s)
Asum.sort()
Bsum.sort()
answer = 0
for i in range(len(Asum)):
    l = bisect.bisect_left(Bsum,T-Asum[i])
    r = bisect.bisect_right(Bsum,T-Asum[i])
    answer+=r-l
print(answer)
