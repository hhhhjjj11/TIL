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
        if not i in idx :
            stack.append((per+[li[i]],idx+[i]))

print(Answer)

