from itertools import permutations 
n,m = map(int,input().split()) # n,m을 입력받는다.

num = sorted(list(map(int,input().split()))) # 입력받은 숫자들을 배열에 sort해서 저장한다.

com = []

com.extend(list(map(' '.join,permutations(map(str,num),m)))) # 출력형태에 맞게 com 이라는 배열에 permutation을 이용해서 저장한다.

for i in range(len(com)): # 조건에 맞게 출력한다.
    print(com[i])
