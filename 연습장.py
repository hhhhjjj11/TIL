# 방향바꿔주는 함수
def changedir(d,r):
    #print('d',d,'r',r)
    if (d =='왼'and r == 'L') or (d == '오' and r == 'D'):
        return '아래'
    if (d =='왼' and r =='D') or (d == '오' and r == 'L'):
        return '위'
    elif (d == '아래' and r == 'L') or (d== '위' and r == 'D'):
        return  '오'
    elif (d == '아래' and r == 'D') or (d == '위' and r =='L'):
        return '왼'

print(changedir('아래','D'))