import sys

l = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

def maketable(pattern): # KMP 알고리즘의 패턴 테이블을 만들어놓고 몇 번째 문자열까지 접두사 접미사가 같은지 확인한다.
    lp = len(pattern)
    table = [0] * lp
    i = 0
    for j in range(1,lp):
        while i > 0 and pattern[i] != pattern[j]:
            i = table[i-1]
        if pattern[i] == pattern[j]:
            i += 1
            table[j] = i
    return table
#print(maketable(s))
print(l-maketable(s)[-1]) # 광고의 길이에서 테이블의 마지막 원소를 뺀다.  