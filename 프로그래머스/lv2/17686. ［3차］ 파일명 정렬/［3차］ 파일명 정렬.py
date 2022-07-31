def solution(files):
    answer = []
    ans = []
    for i in range(len(files)):
        head=''
        number=''
        tail=''
        for j in range(len(files[i])):
            if not number and files[i][j].isdigit()==False:
                head+=files[i][j].lower()
            elif files[i][j].isdigit() and len(number)<6 and not tail:
                number+=files[i][j]
            elif head and number and files[i][j].isdigit()==False:
                tail+=files[i][j].lower()
        ans.append((i,head,int(number),tail))
    ans.sort(key=lambda x:(x[1],x[2]))
    for i in range(len(ans)):
        idx = ans[i][0]
        answer.append(files[idx])
    return answer