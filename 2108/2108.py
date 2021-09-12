from collections import Counter # 최빈값을 구하기 위해서 import 
n = int(input())  # 범위 설정해주는 변수

list = [] 
sum = 0
for i in range(n): # n 개만큼 입력받아서 list에 저장
    list.append(int(input()))

for i in range(len(list)):
    sum += list[i]
avg = round(sum/len(list)) # 평균을 구해준다.

print(avg)
list.sort() # 정렬 후 중앙값 출력
print(list[n//2])

cnt = Counter(list).most_common() # 최빈값 출력을 위한 알고리즘
if len(cnt) == 1:
    print(cnt[0][0])
else:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])

print(list[len(list)-1]-list[0]) # 범위 출력

