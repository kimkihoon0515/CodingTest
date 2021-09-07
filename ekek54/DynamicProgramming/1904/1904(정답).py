import sys
N = int(sys.stdin.readline())
mem= [1,2,3]
def fibonachi(N):
    if N <= 3:
        return mem[N-1]
    for i in range(N-3):
        mem[0] = mem[1]
        mem[1] = mem[2]
        mem[2] = (mem[0]+mem[1])%15746
    return mem[2]
print(fibonachi(N))
# len=3의 배열로 피보나치 구현