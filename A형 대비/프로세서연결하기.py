# 언제 저장을 해야할지 각 코에에서 한번 실행 할때마다.
# 트리를 도식화해서 생각.. 각노드들의 상태를 저장해줘야함. 그러려면 언제 저장해야할까를생각하면됨.
# 어떤걸 저장해야 할지 -> 보드 전체를 저장해야할듯
# 스택에 추가적으로 함께 저장할 것이 있는지 ->
# 행동 : 다음 코어를 
# Q. 굳이 스택에 저장 안해도 되는거 아닌가..?

T = int(input())

def link(board, dir, corenum):
    copied = [board[i][:] for i in range(N)]
    ni,nj,di,dj = cores[corenum][0], cores[corenum][1], dir[0], dir[1]
    k=1
    while True:
        if not (0<=ni+di*k<N and 0<=nj+dj*k<N): # 인덱스 범위를 벗어나면 중지
            break
        if copied[ni+di*k][nj+dj*k]:         # 이미 전선이 있으면
            return (0,0)
        copied[ni+di*k][nj+dj*k] = 1
        k += 1
        
    board_after_link = copied
    lines_to_add = k-1

    return (board_after_link, lines_to_add)


directs = [(1,0),(0,1),(-1,0),(0,-1),(0,0)]   # 상, 하, 좌, 우, 부동

for tc in range(1,T+1):

    N = int(input())
    board = [list(map(int,input().split())) for _ in range(N)]

    core_total_num = 0

    cores = [0]   # core의 (i,j)

    for i in range(1,N-1):
        for j in range(1,N-1):
            if board[i][j]:
                # print(f'##### {i} {j} #####')
                # print('왼',board[i][:j])
                # print('오',board[i][j+1:])
                if 1 in board[i][:j] and 1 in board[i][j+1:] : # 내가 아래에서 짠 로직이 제대로 돌려면, 이 경우는 코어에서 제외해 줘야함. 그렇지 않으면 전부다 막혀있는 코어에가서 다 continue되기때문에 더이상 진행이 안됨. pop만 되고 append가 안됨.
                    temp1=[]
                    temp2=[]
                    for k in range(i):
                        temp1.append(board[k][j])
                    for k in range(i+1,N):
                        temp2.append(board[k][j])
                    # print('위',temp1)
                    # print('아래',temp2)
                    if 1 in temp2 and 1 in temp1:
                        # print('continue')
                        continue
                    core_total_num += 1
                    cores.append((i,j))
                else:
                    core_total_num += 1
                    cores.append((i,j))                            

    stack = [] 

    corenum = 0
    linked= 0
    lines = 0
    stack.append((board, corenum, linked, lines))                     # corenum번의 core까지 계산한 보드.
    
    M_linked = 0
    m_lines = N**2

    while stack:                                                      # DFS + 백트래킹

        board, corenum, linked, lines = stack.pop()
        core_now = corenum + 1
        if corenum == core_total_num:                                # 모든 코어를 다 처리했다면, 
            if linked > M_linked : 
                M_linked = linked
            elif linked == M_linked:            # 연결된 코어갯수가 최대로 같을 경우 전선개수가 작은 것이 답.
                if m_lines > lines:
                    m_lines = lines

        else:
            for dir in directs:                                           # 각 방향에 대해 현재 코어에서 액션처리
                board_after_link, addedline = link(board,dir,core_now)    # link함수에서, 전선이 겹치면 0을 리턴하도록 하자.
                if not board_after_link:                         
                    continue                                              # 함수값이 0인 경우 (전선이 겹치는 경우)에는 그냥 넘어가기.
                linked_after = linked + 1
                lines_after = lines + addedline
                stack.append((board_after_link, core_now, linked_after, lines_after))    # 전선이 겹치지 않는 경우는 스택에 추가한다.
                                                                                         # 참고 : 트리 상에서 다시 위로 올라갈 필요가 없음, 계속 "누적"되므로.
                                                                                         # 따라서, pop한 부모노드를 다시 append할필요가 없음. (좀 더 명확히 정리 필요)
            
    print(f'#{tc} {m_lines}')



"""
  # 아래와 같이 하면 안될 것 같은데.. 이유가 정확히 머지?? clearify하기.
    for core in cores: # 각 코어들에 대해 
        for dir in directs: # 5가지 경우로 
            board_after_link = link(core, dir) # 보드를 바꿔서 리턴하는 함수.
    # 이유 : 다섯가지경우 각각에 대해 다시 다섯가지 경우가 펼쳐져야함. 
    # 근데 저렇게 하면 마지막 dir만 적용된 상태로 다음 코어로 넘어간다..(?) 따라서 기록을해놔야함..(?)

"""

  