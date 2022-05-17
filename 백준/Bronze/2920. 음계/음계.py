import sys

nums = list(map(int,sys.stdin.readline().split()))

if nums == sorted(nums):
    print('ascending')
elif nums == sorted(nums,reverse=True):
    print('descending')
else:
    print('mixed')