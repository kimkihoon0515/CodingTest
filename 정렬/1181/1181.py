n = int(input()) # n 개의 input을 입력받는다.
word = [] # 입력받은 단어들을 배열에 저장한다.
for i in range(n):
    word.append(input())

word = list(set(word)) # 중복을 제거
word.sort() # 알파벳 순으로 정렬
word.sort(key=lambda x: len(x)) # 길이를 기준으로 정렬

for i in range(len(word)):
    print(word[i])