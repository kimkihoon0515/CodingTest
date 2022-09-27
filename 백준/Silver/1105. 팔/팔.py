L, R = input().split()
Llen, Rlen = len(L), len(R)
cnt = 0
if Llen != Rlen :
    print(cnt)
else :
    for i in range(Llen) :
        if L[i] != R[i] :
            break
        else :
            if L[i] == '8' :
                cnt += 1
    print(cnt)