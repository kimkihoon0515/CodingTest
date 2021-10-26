n = int(input())

p = list(map(int,input().split())) # 뒤에 사람이 앞에 사람이 인출하는데 걸리는 시간에 + 되는 방식

p.sort() # 합이 가장 작게 만들려면 가장 작은 수부터 합해 나가야 한다. 그래야 숫자가 큰 것들이 나중에 더해지기 때문이다.
sum = 0
result = 0
for i in range(n):
    sum +=p[i]
    result +=sum
print(result)