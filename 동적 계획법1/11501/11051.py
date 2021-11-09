import math
n1, n2 = map(int, input().split())
ans = math.factorial(n1) // math.factorial(n1-n2) // math.factorial(n2) 
print(ans%10007)