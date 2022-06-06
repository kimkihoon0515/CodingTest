T = int(input())

for _ in range(T):
    N = int(input())
    alcohol = []
    
    for _ in range(N):
        S, L = map(str, input().split())
        alcohol.append([S,int(L)])
        
    alcohol = sorted(alcohol, key = lambda x: x[1])
    print(alcohol[-1][0])