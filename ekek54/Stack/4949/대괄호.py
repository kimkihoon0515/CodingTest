import sys

def VPS(arr):
    while(1):
        if '()' not in arr and '[]' not in arr :
            if len(arr)==0:
                return 'yes'
            else:
                return 'no'
        elif '()' in arr :
            arr = arr.split('()')
            arr = "".join(arr)
        elif '[]'  in arr:
            arr = arr.split('[]')
            arr = "".join(arr)


while(1):
    arr = sys.stdin.readline().rstrip('\n')
    if arr == ".":
        break
    lis=[]
    for i in arr:
        if i == '(' or i == ')' or i == '[' or i == ']':
            lis.append(i)
    lis="".join(lis)
    print(VPS(lis))