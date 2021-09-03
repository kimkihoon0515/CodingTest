a = input()
#print(a)
croa_list = ["c=","c-","dz=","d-","lj","nj","s=","z="]
#print(croa_list)
cnt = 0
for i in croa_list:
    index = a.count(i)
    cnt+=index
count = len(a) - cnt*2
print(count+cnt)
