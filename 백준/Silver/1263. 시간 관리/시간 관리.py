N = int(input())
schedule = []

for _ in range(N):
    T, S = map(int, input().split())
    schedule.append([T, S])

schedule = sorted(schedule, key=lambda x:x[1])


time = 0
while True:
    sumTime = time

    for t, s in schedule:
        if sumTime+t <= s:
            sumTime += t
        else:
            print(time-1)
            exit()
    time += 1