import sys

n = int(sys.stdin.readline())

tree = {}

for _ in range(n):
    root,left,right = sys.stdin.readline().split()
    tree[root] = [left,right]
    
def pre(x): # root,left,right
    if x == '.':
        return
    print(x,end='')
    pre(tree[x][0])
    pre(tree[x][1])
    
def post(x): # left,right,root
    if x == '.':
        return
    post(tree[x][0])
    post(tree[x][1])
    print(x,end='')

def inorder(x): # left,right,root
    if x == '.':
        return
    inorder(tree[x][0])
    print(x,end='')
    inorder(tree[x][1])
    
pre('A')
print()
inorder('A')
print()
post('A')
