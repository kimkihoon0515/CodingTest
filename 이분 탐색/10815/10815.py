import sys

n = int(sys.stdin.readline())
card = list(map(int,sys.stdin.readline().split()))
card.sort()

m = int(sys.stdin.readline())
li = list(map(int,sys.stdin.readline().split()))

def binary(x):
    left = 0
    right = n-1
    
    while left <= right:
        mid = (right+left)//2
        if card[mid] == x:
            return 1
        elif card[mid] > x:
            right = mid-1
        else:
            left = mid+1
    return 0

for i in li:
    print(binary(i))