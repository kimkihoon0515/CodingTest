import re,sys

n = int(sys.stdin.readline())
s,e = sys.stdin.readline().strip().split('*') 

pattern = re.compile(s+'.*'+e+'+')


for _ in range(n):
    string = sys.stdin.readline().strip()
    a = pattern.search(string)
    if a and a.group() == string:
        print('DA')
    else:
        print('NE')