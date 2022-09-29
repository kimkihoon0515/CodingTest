l = int(input())
s = list(map(int,input().split()))
n = int(input())
s.sort()

if n in s:
	print(0)
else:
	cnt = 0
	min_n = 0
	for i in s:
		if i < n:
			min_n = i
		elif i > n:
			max_n = i
			break
			
	for i in range(min_n+1,max_n-1):
		for j in range(i+1,max_n):
			if i <= n and j >= n:
				cnt += 1
	print(cnt)