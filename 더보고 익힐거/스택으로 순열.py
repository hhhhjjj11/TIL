# 두줄요약:
# -> 각 값이랑 사용기록 함께 묶어서 임시보관
# -> 꺼내서 각 재료들에 대해 쓴적없으면 더해서 다시 임시보관함에 넣기


# 1. 스택에 각항들을 저장해놓음. 이때 ([value], [index])로 인덱스도 함께 저장하며, 또 배열의 형태로 저장해줌. (추가할것이기때문)
# 2. 원하는 항의 개수가 될때까지, 각 연결노드마다 [v] [i] 에 어팬드해서 스택에 저장.
# 3. 참고 . 원래배열을건들면 안됨 그러면 그다음 케이스 영향 받음. 배열덧셈으로 추가하여 저장해줌.


# 방문표시를 모두 공유하는 경우 vs 모두 공유하지 않는 경우
# 순열을 구하는 경우는 후자임. (각 항들을 돌려써야하기때문에)
# 이 경우 스택에 저장할때 ★방문표시(인덱스활용)를 함께 저장★해준다.

# 이거는 dfs는아니고,, bfs인듯.
# 근데 굳이말하자면 탐색방향이 다음레벨에서 반대임
#
# dfs 와 bfs 코드상 비교
# 1. dfs 는 밑으로갔다가 찍고 위로 돌아오기때문에
# 뺀거를 도로 넣어야되는데
# bfs는 밑으로만 가니까 pop한거 도로 넣을필요가없다..


li = [1,2,3,4]

stack = [([value],[index]) for index, value in enumerate(li)]

print(stack)

Answer = []

while stack:
    per, idx = stack.pop()

    if len(per) == len(li):
        Answer.append(per)

    for i in range(len(li)):
        if not i in idx:
            stack.append((per+[li[i]],idx+[i]))

print(Answer)




# 이렇게 하면 안됨.
# 핵심 원인 : 리스트(객체도)는 내부의 항을 더하거나 제거해도 전체 참조주소가 계속 일정함.
#           따라서 "리스트를 바인딩한 변수"를 스택에 담아서 쓸때는 얕은복사로 인한 오류가 나는 것을 특히 조심해야함.

li = [1,2,3,4]

# 아이디어. 기록서랑 퍼뮤랑 묶어서 임시보관. -> 꺼내서 재료중에 기록서에 표시안된애들 추가해서 저장

stack = [([],[0]*len(li))]
# 리스트와 딕셔너리의 경우 항목을 추가하거나 제거해도 참조주소가 계속 같음.
# 따라서 변화를 시켜도 얕은 복사가 이루어짐.
results = []
while stack:
    permu, used = stack.pop()
    if len(permu) == len(li):
        results.append(permu)
        continue
    for i in range(len(li)):
        if not used[i]:
            used[i] = 1
            # 여기서 used의 주소와
            stack.append((permu+[li[i]],used))
            # 여기서 used의 주소가 같음.
            used[i] = 0
            # 즉, 20줄에서 used[i]=0 을 쓰면 스택에 들어있는 used의 i번째 항도 0이 됨.
