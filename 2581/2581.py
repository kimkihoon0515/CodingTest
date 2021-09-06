m = int(input())
n = int(input())

def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True
first_number=0
sum = 0
cnt = 0
for i in range(m,n+1):
    if is_prime_number(i) == True:
        cnt+=1
        if cnt == 1:
            first_number = i
        sum+=i
    else:
        cnt+=0
if cnt==0:
    print(-1)
else:
    print(sum)
    print(first_number)

        