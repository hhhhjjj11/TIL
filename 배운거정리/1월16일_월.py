#슬라이싱 (연습 많이 해줘야 함!)
s = 'abcdefgh'
#cde 만 빼고 출력해라 ( index: 2,3,4 ) 
print(s[0:2]+s[5:7])
# 처음과 끝은 생략가능
print(s[:2]+s[5:])


#비시퀀스형 컨테이너
di = {}
di = dict()

#딕셔너리에 key, value추가
di['name'] = '허재'

# 전체 조회
print(di) # {'name': '허재'}

# 특정 key 조회
print(di['name'])
print(di.get('name'))

# di['nothing'] = keyError발생 
# di.get('nothing')
print(di.get('nothing'))
print('여기까지 오나요?')

# list vs dictionary
li = [
    ['사람이름1',23],
    ['사람이름2',24],
    ['사람이름3',26]
]

di = {
    'names':['사람이름1','사람이름2','사람이름3'],
    'ages':[23,24,26],
    'people':
        ['사람이름1', 23]
    
}

