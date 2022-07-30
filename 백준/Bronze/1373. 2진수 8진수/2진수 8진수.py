import sys

n = str(sys.stdin.readline().strip())
a = int('0b'+n,2)
print(oct(a)[2:])