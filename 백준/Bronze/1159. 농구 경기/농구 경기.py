from collections import Counter
n = int(input())
player = []
fn = []
cnt = 0
for i in range(n):
    a = input()
    player.append(a[0])
player_count = Counter(player)
for i, j in player_count.items():
    if j >= 5:
        fn.append(i)
        cnt += 1
fn.sort()
if cnt == 0:
    print("PREDAJA")
else:
    for i in fn:
        print(i, end='')