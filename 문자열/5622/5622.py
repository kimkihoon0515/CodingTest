a = list(map(str,input())) # 배열을 입력받는다.
b = [] # 숫자로 바꿔서 저장하기 위한 배열
sum = 0 # 합을 구하는 변수 선언
for i in range(len(a)): # a의 배열의 길이만큼 반복
    if(a[i]=="W" or a[i]=="X" or a[i]=="Y" or a[i]=="Z"): # 조건에 따라 숫자를 정하고 b의 배열에 넣는다.
        b.append("10")
    elif(a[i]=="T" or a[i]=="U" or a[i]=="V"):
        b.append("9")
    elif(a[i]=="P" or a[i]=="Q" or a[i]=="R" or a[i]=="S"):
        b.append("8")
    elif(a[i]=="M" or a[i]=="N" or a[i]=="O"):
        b.append("7")
    elif(a[i]=="J" or a[i]=="K" or a[i]=="L"):
        b.append("6")
    elif(a[i]=="G" or a[i]=="H" or a[i]=="I"):
        b.append("5")
    elif(a[i]=="D" or a[i]=="E" or a[i]=="F"):
        b.append("4")
    elif(a[i]=="A" or a[i]=="B" or a[i]=="C"):
        b.append("3")
    sum +=int(b[i]) # 합을 구해준다.
print(sum)