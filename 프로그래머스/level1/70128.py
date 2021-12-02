def solution(a, b): 
    answer = sum(x*y for x,y in zip(a,b))
    return answer
# zip(a,b) => a,b에 속해있는 것들을 순서대로 짝짓는다. 
# ex) a = [1,2,3] b = [4,5,6] 
# zip(a,b) => (1,4), (2,5), (3,6) 으로 만들어진다.