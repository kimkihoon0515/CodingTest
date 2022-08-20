import sys

n,p = map(int,sys.stdin.readline().split())

op = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

hash = {}

cnt = 0
for string,flat in op:
    if string not in hash:
        hash[string] = []

    if not hash[string] or hash[string][-1] < flat:
        hash[string].append(flat)
        cnt +=1

    elif hash[string] and hash[string][-1]> flat:
        while True:
            if not hash[string]:
                hash[string].append(flat)
                cnt+=1
                break
            else:
                if hash[string] and hash[string][-1]>flat:
                    hash[string].pop(-1)
                    cnt+=1
                    
                if hash[string] and hash[string][-1]<flat:
                    hash[string].append(flat)
                    cnt+=1
                    break

                if hash[string] and hash[string][-1] == flat:
                    break

print(cnt)