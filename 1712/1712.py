a = list(map(int,input().split()))
cnt = 1
while cnt:
    cost = a[0] + cnt *a[1]
    price = a[2]
    if price * cnt - cost >0:
        break
    elif price < a[1]:
        cnt = -1
        break
    else:
        cnt+=1
print(cnt)