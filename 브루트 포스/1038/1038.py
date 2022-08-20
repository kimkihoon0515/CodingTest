import sys

n = int(sys.stdin.readline())

# 0~9876543210 까지

def solution(n):
    if n >=1023:
        return -1
    elif n == 0:
        return 0
    else:
        num = 1
        cnt = 0
        while True:
            s = str(num)
            flag = True
            if len(s) == 1:
                pass
            else:
                for i in range(1,len(s)):
                    if int(s[i])<int(s[i-1]):
                        continue
                    else:
                        start = s[:i-1]
                        mid = str(int(s[i-1])+1)
                        end = '0'+s[i+1:]
                        num  = int(start+mid+end)
                        flag = False
                        break
            if flag:
                cnt+=1
                if cnt == n:
                    return num
                num+=1

print(solution(n))