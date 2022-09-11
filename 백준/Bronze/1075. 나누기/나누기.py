import sys

n = sys.stdin.readline().strip()
f = int(sys.stdin.readline())

a = int(n[:-2]+'00')

while True:
    if a % f == 0:
        break
    a+=1
print(str(a)[-2:])