N=int(input())
L=[]
for i in range(N):
    word=input()
    L.append(word)

L.sort(key=len)
ans=0
for i in range(N):
    nowWord=L[i]
    isHead=False
    for j in range(i+1,N):
        try:
            if L[j].index(nowWord)==0:
                isHead=True
                break
        except:
            continue
    if not isHead:
        ans+=1
print(ans)