def solution(n, arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        arr1[i] = int(bin(arr1[i])[2:]) # int형 2진수로 변경
        arr2[i] = int(bin(arr2[i])[2:])
        
    for i in zip(arr1,arr2):
        answer.append(sum(i)) # 두 수의 합을 저장
    ans = []
    
    for i in answer:
        s = ''
        if len(str(i))!=n: # i의 길이가 n보다 작으면
            cnt = n-len(str(i))
            s += ' '*cnt # 길이의 차이만큼 공백문자를 넣는다.
        for j in str(i):
            if j == '0': # 0이면 공백을
                s += ' '
            else: # 다른거면 #을 넣는다.
                s += '#'
        ans.append(s)
    return ans