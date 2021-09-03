a = list(map(str,input().split()))
print(a)
croa_list = ["c=","c-","dz=","d-","lj","nj","s=","z="]
print(croa_list)
cnt = 0
count = 0
for i in croa_list:
    for j in a:
        if i in j:
            cnt+=1
print(cnt)