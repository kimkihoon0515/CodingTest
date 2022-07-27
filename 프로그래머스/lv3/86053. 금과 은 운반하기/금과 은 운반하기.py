def solution(a, b, g, s, w, t): # 금 : a 은 : b 편도 : t 최대 : w
    answer = -1
    start = 0
    end = 10**9 * 10**5 *4
    
    while start<=end:
        mid = (start+end)//2
        current_gold = 0
        current_silver = 0
        total = 0
        
        for i in range(len(t)):
            cnt = (mid-t[i])//(t[i]*2)+1
            
            if cnt * w[i]>g[i]:
                current_gold +=g[i]
            if cnt * w[i]<=g[i]:
                current_gold += cnt*w[i]
            if cnt * w[i]>s[i]:
                current_silver +=s[i]
            if cnt * w[i]<=s[i]:
                current_silver += cnt*w[i]
            if s[i]+g[i] < cnt*w[i]:
                total += s[i]+g[i]
            if s[i]+g[i] >= cnt*w[i]:
                total += cnt*w[i]
        if current_gold>=a and current_silver>=b and total>=a+b:
            end = mid-1
            answer = mid
        else:
            start = mid +1
    return answer