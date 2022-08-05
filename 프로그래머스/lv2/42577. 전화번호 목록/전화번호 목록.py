'''
# 100만이므로 O(nlogn)가능 -> 시간초과.. 너무 복잡하게 생각하지 말것
def solution(phone_book):
    answer = True
    phone_book.sort(key=lambda x:len(x))
    hash = {}
    n = len(phone_book)
    for i in range(n):
        if phone_book[i] not in hash:
            hash[phone_book[i]] = []
        number = i+1
        while number < n:
            hash[phone_book[i]].append(phone_book[number][:len(phone_book[i])])
            number+=1
    for key,value in hash.items():
        if key in value:
            answer = False
        
    return answer
'''
def solution(phone_book):
    answer = True
    hash = {}
    for number in phone_book:
        hash[number] = 1
    
    for phone_number in hash:
        s = ''
        for i in phone_number:
            s+=i
            if s in hash and s !=phone_number:
                answer = False
    
    return answer