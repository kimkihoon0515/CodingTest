def solution(s):
    answer = []
    for word in s:
        cnt = 0
        new_word = ''
        for i in range(len(word)):
            if word[i] == '0' and new_word[-2:] == '11':
                cnt +=1
                new_word = new_word[:-2]
            else:
                new_word+=word[i]
        index = new_word.find('11')
        if index == -1:
            index2 = new_word.rfind('0')
            new_word = new_word[:index2+1] + '110'*cnt + new_word[index2+1:]
        else:
            new_word = new_word[:index]+'110'*cnt+new_word[index:]
        answer.append(new_word)
    return answer