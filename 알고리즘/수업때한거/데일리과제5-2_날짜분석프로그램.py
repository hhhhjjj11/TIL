# 입력 예시
# 2015
# 8
# 31

# 출력 예시 
# 경고 월요일입니다.
# {'년': 2015, '월': 8, '일': 31, '요일': '월요일'}

import calendar

Y = int(input())
isYoon = True
while isYoon:
    if (Y % 4 ==0 and Y%100 !=0) or (Y%4==0 and Y%400==0):
        print('윤년입니다. 연도를 다시 입력해주세요')
        Y=int(input())
    else:
        isYoon=False

print(calendar.calendar(Y))

M = int(input())
D = int(input())

#formatyear(theyear, w=2, l=1, c=6, m=3)

요일={
    '0':'월요일',
    '1':'화요일',
    '2':'수요일',
    '3':'목요일',
    '4':'금요일',
    '5':'토요일',
    '6':'일요일'

}

dic={}
dic['년']=Y
dic['월']=M
dic['일']=D
dic['요일']=요일[str(calendar.weekday(Y, M, D))]
if calendar.weekday(Y, M, D)==0:
    print('경고 월요일입니다.')
    print(dic)
