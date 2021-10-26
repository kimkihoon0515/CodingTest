import sys

a,b,c = map(int,sys.stdin.readline().split())

print(pow(a,b,c)) # pow(x, y) is equal to xy pow(x, y, z) is equal to xy % z