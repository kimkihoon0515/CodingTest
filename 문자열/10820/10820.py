import sys 
while True: 
    line = sys.stdin.readline().rstrip('\n') 
    up, lo, sp, nu = 0, 0, 0, 0 
    if not line: 
        break 
    for l in line: 
        if l.isupper(): 
            up += 1 
        elif l.islower(): 
            lo += 1 
        elif l.isdigit(): 
            nu += 1 
        elif l.isspace(): 
            sp += 1 
    sys.stdout.write("{} {} {} {}\n".format(lo, up, nu, sp))

