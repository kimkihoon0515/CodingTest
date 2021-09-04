a = int(input()) # 몇 개의 자료를 입력받을지 정한다.

for i in range(a):
    h, w, n = map(int,input().split()) # h:높이 w: 너비 n: n번째 손님
    f = n % h # 층수는 명수를 높이로 나눈 나머지이다.
    room = n // h +1 # 소수점을 버린고 +1을 한다.
    if f == 0: # 명수와 높이가 같으면 room 에서 1씩 빼고 층수는 높이와 같다.
        room -=1
        f = h
    print(f * 100 + room)