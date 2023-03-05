"""
스택에 저장할 것 = 보드, 취급할 코어(번호로구분), 연결된코어갯수, 전선길이
까다로운 조건1 : "연결이 안되는 프로세서가 있을수도 있다" -> 연결을 안하는 경우도 dfs의 케이스에 넣어주어야함.
-> 이 경우 코어번호만 증가시켜서 넘긴다. -> 코어번호만 증가시켜서 다시 스택에 넣는다.
까다로운 조건2 : 방향에 따라 연결이 되는 방향이 있고 안되는 방향이 있는데, 이때 연결 안되는 방향은 continue로 넘길경우,
네 방향 전부에서 막혀있는 프로세스의 경우에서는 더이상 진행이 안되고 pop만 됨. 
-> 그래서 모든 방향에서 연결이 안될경우 따로 취급하여 코어번호를 1증가시켜서 스택에 다시 넣어주는 로직을 추가해줘야함.
"""

T = int(input())

directs = [(1,0),(0,1),(-1,0),(0,-1),(0,0)]     # 상, 하, 좌, 우, 부동

def link(board, dir, corenum):
    copied = [board[i][:] for i in range(N)]
    ni,nj,di,dj = cores[corenum][0], cores[corenum][1], dir[0], dir[1]
    k=1
    while True:
        if not (0<=ni+di*k<N and 0<=nj+dj*k<N): # 인덱스 범위를 벗어나면 중지
            break
        if copied[ni+di*k][nj+dj*k]:            # 이미 전선이 있으면
            return (0,0)
        copied[ni+di*k][nj+dj*k] = 1
        k += 1
    board_after_link = copied
    lines_to_add = k-1
    return (board_after_link, lines_to_add)

for tc in range(1,T+1):
    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]
    core_total_num = 0
    cores = [0]   # core의 (i,j)
    for i in range(1,N-1):
        for j in range(1,N-1):
            if board[i][j]:
                core_total_num += 1
                cores.append((i,j))    
    stack = [] 
    corenum, linked, lines = 0, 0, 0
    stack.append((board, corenum, linked, lines))                     # corenum번의 core까지 계산한 보드.

    M_linked = 0
    m_lines = N**2

    while stack:                                                      # DFS + 백트래킹
        board, corenum, linked, lines = stack.pop()
        core_now = corenum + 1
        if corenum == core_total_num:                                # 모든 코어를 다 처리했다면, 
            if linked > M_linked : 
                M_linked = linked
                m_lines = lines
            elif linked == M_linked:            # 연결된 코어갯수가 최대로 같을 경우 전선개수가 작은 것이 답.
                if m_lines > lines:
                    m_lines = lines
        else:
            islinked = False
            for dir in directs:                                           # 각 방향에 대해 현재 코어에서 액션처리
                if dir ==(0,0):                                            # 이 경우 현재코어에 연결하지 않고 그냥 넘어가는거임. 코어번호만 다음으로 넘긴다.  
                    stack.append((board,core_now,linked,lines))
                    continue
                board_after_link, addedline = link(board,dir,core_now)    # link함수에서, 전선이 겹치면 0을 리턴하도록 하자.
                if not board_after_link:                                  # 추가해야할 조건 : 만약에, 모든 방향에 대해 연결할 수 없다면 ->
                    continue                                              #  for dir in directs에서 아무것도 안하고 끝나는거라서 스택에서 뽑은거는 걍 버려지는거임★★★.
                stack.append((board_after_link, core_now, linked + 1, lines+addedline))       # 근데 그러면 안되고, 그 다음 프로세서를 따져줘야하는 거니까. 그렇게 하기위해서,
                islinked = True                                           # ★만약 모든방향에서 연결할 수 없다면 다음번 코어넘버를 1더한다음 다시 스택에 넣어주면 됨.★
            if not islinked:
                stack.append((board,core_now,linked,lines))               # 함수값이 0인 경우 (전선이 겹치는 경우)에는 그냥 넘어가기.
                                                                          # 전선이 겹치지 않는 경우는 스택에 추가한다.
    print(f'#{tc} {m_lines}')                                          # 참고 : 트리 상에서 다시 위로 올라갈 필요가 없음, 계속 "누적"되므로.
                                                                    # 따라서, pop한 부모노드를 다시 append할필요가 없음. (좀 더 명확히 정리 필요)
    
    



"""
  # 아래와 같이 하면 안될 것 같은데.. 이유가 정확히 머지?? clearify하기.
    for core in cores: # 각 코어들에 대해 
        for dir in directs: # 5가지 경우로 
            board_after_link = link(core, dir) # 보드를 바꿔서 리턴하는 함수.
    # 이유 : 다섯가지경우 각각에 대해 다시 다섯가지 경우가 펼쳐져야함. 
    # 근데 저렇게 하면 마지막 dir만 적용된 상태로 다음 코어로 넘어간다..(?) 따라서 기록을해놔야함..(?)

"""

  