import sys

# 좋은 수열 / 나쁜 수열 확인 함수
def isGoodArr(arr):
    arr_len = len(arr)				# 수열 길이
    for part_len in range(1, arr_len // 2 + 1):	# 비교할 부분수열의 길이
        # 부분수열 비교 시작
        for part_start in range(part_len, arr_len - part_len + 1):
            # 같은 부분수열 발견하면
            if arr[part_start - part_len:part_start] == arr[part_start:part_start + part_len]:
                return False			# False 리턴
    else:					# 모든 부분수열이 다르면
        return True				# True 리턴

# 백트래킹
def dfs(arr, depth):
    if depth == N:				# 원하는 길이가 되면 
        print("".join(list(map(str, arr))))	# 수열 출력
        sys.exit()				# 종료
    arr.append(1)				# 1 추가 (아무 수나 상관 없음)
    for i in range(1, 4):			# 1부터 3까지 반복
        arr.pop()
        arr.append(i)
        if isGoodArr(arr):			# 해당 수열이 좋은 수열이면
            if not dfs(arr, depth + 1):		# 다음 다리 수 시작
            # 만약 다음 자리 수에서 1~3 모두 넣어도 좋은 수열이 없다면 현재 자리수 1 증가
                continue			
    else:
        # 현재 자리 수 1~3 모두 넣어도 좋은 수열이 없는 경우
        arr.pop()				# 이번 자리 수 없앰
        return False				# False 리턴


N = int(input())				# 입력
dfs([1], 1)			