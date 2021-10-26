n = int(input()) # n 번째 줄까지의 입력을 받는다.

def draw(x):
    pattern=[]
    for i in range(3 *len(x)):
        if i // len(x) == 1:
            pattern.append(x[i % len(x)]+ " " * len(x) + x[i % len(x)])
        else:
            pattern.append(x[i % len(x)] * 3)
    return pattern

star = ["***", "* *", "***"]
k = 0

while n !=3 :
    n = int(n//3)
    k+=1

for i in range (k):
    star = draw(star)

for i in star:
    print(i)