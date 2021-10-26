# 상당히 어려워진다.
import sys
input = sys.stdin.readline
"""
 table[i][j] = table[i][j-1] + page[j] + min(minimum) 를 이용해서 풀어야한다.
 각각 계산되는 비용은 다음과 같다.

 

(page[0] + page[1]) + page[2]

: (40 + 30) + (70 + 30) # 첫 번째 합의 비용 40+30 = 70, 이후 두 번째 합의 비용 70+30 = 100

page[0] + (page[1] + page[2])

: (30 + 30) + (60 + 40) # 첫 번째 합의 비용 30+30 = 6-, 이후 두 번째 합의 비용 60+40 = 100

 

보다시피 첫 번째 합의 비용은 다르지만 두 번째 합의 비용은 100으로 같다. 그 이유는 결국에 마지막 합의 비용은 0부터 2까지의 모든 수를 더한 값과 같기 때문이다.

따라서 최솟값을 결정해주는 것은 마지막 합의 비용이 아닌 그 이전의 비용이다. 그 부분이 min(minimum)을 통해서 구할 수 있도록 해주었다. minimum에는 (table[i][k] + table[k+1][j]) 의 값들이 들어가게 된다. 이 값들이 의미하는 것은 ((i~k까지 더한 비용의 최솟값) + (k+1~j까지 더한 비용의 최솟값))이고, subproblem 으로 나눠서 생각할 수 있게 되었으니 DP로 충분히 해결할 수 있는 문제가 되었다.


결국 dp를 이용해 대각선 방향으로 채워주는 방식으로 전체의 최소 비용을 구할 수 있게 된다.

"""
for i in range(int(input())):
    n = int(input())
    f = list(map(int,input().split()))
    d = [[0]*(n+1) for i in range(n+1)]
    
    for i in range(n-1):
        d[i][i+1] = f[i] + f[i+1]
        for j in range(i+2,n):
            d[i][j] = d[i][j-1] + f[j]

    for v in range(2,n):
        for i in range(n-v):
            j = i+v
            d[i][j] += min([d[i][k] + d[k+1][j] for k in range(i,j)])
    
    print(d[0][n-1])