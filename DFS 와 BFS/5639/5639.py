"""
전혀 어떤 식으로 접근해야하는지 몰라서 코드 참고함
"""
import sys
sys.setrecursionlimit(100000)

pre= []

while True:
    try:
        pre.append(int(sys.stdin.readline()))
    except:
        break

def post(start,end):
    if start > end :
        return 
    
    root = pre[start] # 루트보다 크면 오른쪽 서브트리이다.
    index = start + 1

    while index <= end:
        if pre[index] > root:
            break
        index += 1
    
    post(start+1,index-1)
    post(index,end)
    print(root)

post(0,len(pre)-1)