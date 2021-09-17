n = int(input())
a = list(map(int,input().split()))
add,sub,mul,div = map(int,input().split())

minimum = 1000000000
maximum = -1000000000

def cal(num,i,add,sub,mul,div):
    global minimum,maximum
    if i == n:
        minimum = min(minimum,num)
        maximum = max(maximum,num)
        return

    if add > 0:
        cal(num+a[i],i+1,add-1,sub,mul,div)
    elif sub > 0 :
        cal(num-a[i],i+1,add,sub-1,mul,div)
    elif mul > 0 :
        cal(num*a[i],i+1,add,sub,mul-1,div)
    elif div > 0 :
        cal(int(num/a[i]),i+1,add,sub,mul,div-1)
cal(a[0],1,add,sub,mul,div)
print(maximum)
print(minimum)

