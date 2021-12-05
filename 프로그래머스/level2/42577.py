def solution(phone_book):
    answer = True
    phone_book.sort() # 숫자 순으로 나열하여 최대한 비슷한것 끼리 정렬한다.
    #print(phone_book)
    for i in range(len(phone_book)-1):
        if phone_book[i]==phone_book[i+1][:len(phone_book[i])]: # i가 무조건 i+1번째보다 길이가 작거나 같으므로 길이 비교를 할 때 i번째 원소의 길이만큼 비교해서 같으면 False 반환
            answer = False
    return answer