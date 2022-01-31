import sys

w = sorted([int(sys.stdin.readline().strip()) for _ in range(10)],reverse = True)
k = sorted([int(sys.stdin.readline().strip()) for _ in range(10)], reverse = True)

print(w[0]+w[1]+w[2],k[0]+k[1]+k[2])

