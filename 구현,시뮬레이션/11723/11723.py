import sys
input = sys.stdin.readline
 
empty_set = set()
 
def add(x):
    empty_set.add(x)
 
def remove(x):
    empty_set.discard(x)
 
def check(x):
    if x in empty_set:
        return 1
    return 0
 
def toggle(x):
    if x in empty_set:
        empty_set.discard(x)
    else:
        empty_set.add(x)
 
def set_all():
    global empty_set
    empty_set = {i for i in range(1, 21)}
 
def empty():
    empty_set.clear()
 
for _ in range(int(input())):
    command = input().split()
    if command[0] == 'add':
        add(int(command[1]))
    elif command[0] == 'remove':
        remove(int(command[1]))
    elif command[0] == 'check':
        print(check(int(command[1])))
    elif command[0] == 'toggle':
        toggle(int(command[1]))
    elif command[0] == 'all':
        set_all()
    else:
        empty()