from collections import Counter
n = int(input()) 

list = []
sum = 0
for i in range(n):
    list.append(int(input()))

for i in range(len(list)):
    sum += list[i]
avg = round(sum/len(list))

print(avg)
list.sort()
print(list[n//2])

cnt = Counter(list).most_common()
if len(cnt) == 1:
    print(cnt[0][0])
else:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])

print(list[len(list)-1]-list[0])

