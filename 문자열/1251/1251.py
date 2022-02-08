import sys

s = list(sys.stdin.readline().strip())

ans = []

for i in range(1,len(s)-1): # 1~len(s)-1까지
    for j in range(i+1,len(s)): # i+1부터 s길이까지
        a = s[:i] 
        b = s[i:j]
        c= s[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        ans.append(a+b+c) # ans 배열에 담고
ans.sort() # 사전순으로 정렬
print(''.join(ans[0]))