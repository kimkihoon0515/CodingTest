import sys

board = sys.stdin.readline().strip()

board = board.replace('XXXX','AAAA')
board = board.replace('XX','BB')

if 'X' in board:
    print(-1)
else:
    print(board)