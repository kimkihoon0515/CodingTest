from itertools import combinations

nums=[]
lotto=[]
while(True):
    n = list(map(int,input().split()))
    if n[0] == 0:
        break
    else:
        for i in range(len(n)-1):
            nums.append(n[i+1])
    lotto.append(list(combinations(nums,6)))
    print(lotto[0])
    for i in range(len(lotto)):
        print(lotto[0])
        print()
    nums.clear()
    lotto.clear()
