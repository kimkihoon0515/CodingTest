def a1(a):
    a = a+1


def a2(s):
    s[0] = s[0]+1


a = 3

s = [3]
a1(a)
a2(s)
print(a)
print(s)