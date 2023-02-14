# 알아두기 1 . 배열의 각항에 튜플을 이용해서 정보 추가해서 재할당해주는 스끼르
# 알아두기 2 . sorted쓸때 ( lambda : (x[1], x[0])) 의 활용
# 알아두기 3 . 이때 x[0]은 각 항의 첫문자가아니라 문자 전체이고 x[1]은 문자열길이임
            #   이런식으로 문자전체로 잡아줘야만 두번째 세번째 쭉쭉 알파벳 기준으로 정렬가능
            # 그렇지 않으면 첫문자 기준으로밖에 정렬 못함.


N = int(input())

li =[]
for _ in range(N):
    li.append(input())

li = set(li)
li = list(li)

for i in range(len(li)) :
    li[i] = ( li[i], len(li[i]) )

li= sorted(li, key = lambda x : (x[1],x[0]) )

for item in li:
    print(item[0])    


