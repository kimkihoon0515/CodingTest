N = map(int, input().split())

A =set(map(int, input().split()))
B = set(map(int, input().split()))

res = []
for n in A:
    if n not in B:
        res.append(n)

res.sort()
print(len(res))

if len(res) !=0:
    print(*(res))