n = int(input())
a = list(input()) # 첫 번째 문자열

a_len = len(a)
for i in range(n - 1):
    b = list(input()) # 그 다음 문자열부터 비교해서 같으면 그대로 아니면 ? 로 변경
    
    for j in range(a_len):
        if a[j] != b[j]:
            a[j] = '?'
print(''.join(a))