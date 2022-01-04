import sys

n,m = map(int,sys.stdin.readline().split())

dna = list(sys.stdin.readline().strip() for _ in range(n))

cnt, sum = 0, 0 
result = '' 
for i in range(m): 
    a, c, g, t = 0, 0, 0, 0 
    for j in range(n): 
        if dna[j][i] == 'T': 
            t += 1 
        elif dna[j][i] == 'A': 
            a += 1 
        elif dna[j][i] == 'G': 
            g += 1 
        elif dna[j][i] == 'C': 
            c += 1 
    if max(a,c,g,t) == a: 
        result += 'A' 
        sum += c + g +t 
    elif max(a,c,g,t) == c: 
        result += 'C' 
        sum += a + g +t 
    elif max(a,c,g,t) == g: 
        result += 'G' 
        sum += a + c +t 
    elif max(a,c,g,t) == t: 
        result += 'T' 
        sum += c + g + a 
print(result) 
print(sum)