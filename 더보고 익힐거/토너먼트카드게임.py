T = int(input())

def div(li):
    #print('함수실행')
    length = len(li)
    if length > 2:
        li1= li[:(length-1)//2+1]
        li2= li[(length-1)//2+1:]
        li[0] = li1
        li[1] = li2
        while len(li)>2:
            li.pop()
    
    done = True
   
    for i in range(len(li)):
        if len(li[i]) > 2 :
               done =False
        
    if not done:
        for i in range(len(li)):
            div(li[i])
    #print('li',li)

# 이거는 ㅅㅂ [[1,2],[3,4]] 를 [1,3] 으로바꾸러면 
# li[0] = li[0][0] , li[1] = li[1][0] 이런 로직이 있어야함.
# 그래서 이거는 배열의 인덱스 i가 필요하기 때문에
# 이차원배열을 인풋으로 받아야됨. 

def Winner(li):
    
    if type(li[0]) == list and type(li[0][0]) != list:
        for i in range(2):
            if len(li[i]) == 2:
                if (li[i][0][0] - li[i][1][0]) in (1, -2):
                    li[i] = li[i][0]
                elif li[i][0][0]== li[i][1][0]:
                    li[i] = li[i][0]
                else:
                    li[i] = li[i][1]
            else:
                li[i] = li[i][0]

    elif type(li[0]) == list and type(li[0][0]) == list:
        for i in range(len(li)):
            Winner(li[i])

    else:
        if (li[0][0] - li[1][0]) in (1,-2):
            return li[0][1]
        elif li[0][0] == li[1][0]:
            return li[0][1]
        else:
            return li[1][1]


for tc in range(1,T+1):
    res = 0
    N = int(input())
    li = list(map(int,input().split()))
    li = [(value,index) for index,value in enumerate(li)] 

    div(li)
    print(li)

    while type(Winner(li)) != int:
        Winner(li)
    
    A = Winner(li)

    print(f'#{tc} {A+1}')