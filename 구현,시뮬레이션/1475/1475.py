import sys
import math
N = sys.stdin.readline().strip()

list1 = list(map(int, N))
list2 = [0 for _ in range(10)]

for i in list1:
  list2[i] += 1

list2[6] = list2[9] = math.ceil((list2[6]+list2[9])/2)
print(max(list2))