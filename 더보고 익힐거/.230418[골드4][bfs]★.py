# 1단계 : 벽을 세우기                                   / 2단계 : 바이러스 퍼트리기 / 
# 맵이리셋 되어야 함, 다르게말하면 맵별로 케이스가 나뉜다. / Q. 각 맵또한 case가 나눠져서 덱에 들어가야하는가. 이 문제는 그럴 필요가 없다. /

# 1단계 : 벽세우기 
# (케이스나누기 bfs아님, 조합)/ 
# - 벽을 세울 수있는 항들을 리스트로 뽑아낸다음
# - 그 리스트의 인덱스를 가지고 조합을 구한다.

# 2단계 : 바이러스 퍼트리기(바이러스 )/
# 탐색할때 다른 상황을 넣다 뺐다 하니까 맵 또한 case가 나눠져서 덱의 각 항과 함께 저장되어야 할 것같지만. 
# 원래는 각 탐색마다 다르기 때문에 함께 저장하긴 해야함. 
# 이 문제의 경우 각 항에 맵을 각각 저장할 필요가 없음.

# 탐색과정에서 뭐가 갈리는게 없기때문에. 
# 탐색이 끝난후에 세기만 하면 되기때문에.

# 왜냐하면 어차피 가능한 전부 다 확장시킬것이기때문에, 그리고 결국 순서만다르고 그 결과는 똑같을 것이기 때문에.. 말하자면 결과만 중요하지 그 과정은 노상관.
# 그렇기 때문에 맵을 나눌필요가 없다.




n, m = map(int,input().split())

map = [list(map(int,input().split())) for _ in range(n)]

source = []
walls = 0

for i in range(n):
    for j in range(m):
        if map[i][j] == 0:
            source.append((i,j))
        elif map[i][j] == 1:
            walls += 1

sz = len(source)

stack1 = [([i],i) for i in range(sz)]

combis = []

while stack1:
    combi, i = stack1.pop()
    if len(combi) == 3:
        combis.append(combi)
        continue
    for k in range(i+1, sz):
        stack1.append((combi+[k], k))

res = 0

for combi in combis:
    x1,x2,x3 = combi
    i1,j1 = source[x1]
    i2,j2 = source[x2]
    i3,j3 = source[x3]

    map[i1][j1], map[i2][j2], map[i3][j3] = 1, 1, 1

    # 이제 바이러스를 퍼뜨릴건데, 초기 스택에는 바이러스의 위치가들어가고, 퍼뜨린다. 
    # 스택에 담을 것 = 퍼트릴수있는 공간의 좌표
    # 이 문제에서는, 각 스택의 항에 맵을 함께 저장해 둘 필요가 없다는점 알고가자.
    # 왜냐하면, 결국 전부다 퍼트린다음에 결과 몇군데가 전염됬는지가 중요한데, 탐색과정은 달라져도 어차피 모두 진행된 결과는 하나뿐이기때문에. (가능한 모든 영역에 바이러스가 퍼진 결과는 주어진 map 당 오직 하나이다.)

    visited = [[True]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if map[i][j] == 0:
                visited[i][j] = False

    stack2 = []

    for i in range(n):
        for j in range(m):
            if map[i][j] == 2:
                stack2.append((i,j))
                visited[i][j] = True

    while stack2:

        ni, nj = stack2.pop()

        for di,dj in [(1,0),(0,1),(-1,0),(0,-1)]:
            nexti, nextj = ni+di, nj+dj
            if 0 <= nexti <n and 0 <= nextj <m and not visited[nexti][nextj] and map[nexti][nextj] == 0:
                stack2.append((nexti,nextj))
                visited[nexti][nextj] = True # 바이러스가 퍼진곳이 true가 됨 

    cnt = 0 
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                cnt += 1
    
    res = max(cnt,res)

    map[i1][j1], map[i2][j2], map[i3][j3] = 0, 0, 0

print(res)