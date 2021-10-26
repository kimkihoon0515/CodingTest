a = list(map(int,input().split())) # 배열을 입력받는데 공백으로 구분짓는다.
b = int(str(a[0])[::-1]) # a의 첫번째 배열을 뒤집어서 b에 넣는다.
c = int(str(a[1])[::-1]) # a의 두번째 배열을 뒤집어서 c에 넣는다.
if b > c: # 크기를 비교해서 큰 것을 출력한다.
    print (b)
else:
    print (c)