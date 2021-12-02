import datetime
def solution(a, b):
    # 2016년 a월 b일이 무슨 요일인지
    day = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    answer = ''
    answer = day[(sum(month[:a-1])+b)%7]
    return answer