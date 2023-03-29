King, Stone, N = input().split()
N = int(N)
li = [input() for _ in range(N)]

row = [0,'A','B','C','D','E','F','G','H']
moves = {
    'R':(0,1),
    'L':(0,-1),
    'B':(-1,0),
    'T':(1,0),
    'RT':(1,1),
    'LT':(1,-1),
    'RB':(-1,1),
    'LB':(-1,-1)
}

nj , ni = list(King)
sj , si = list(Stone)
ni = int(ni)
nj = row.index(nj)
si = int(si)
sj = row.index(sj)

# print('킹', ni,nj)
# print('돌', si,sj)

for i in range(N):
    MOVE = li[i]
    # print('!', MOVE)
    mi, mj = moves[MOVE]
    nexti = ni + mi            # 다음자리
    nextj = nj + mj
    if not (1<=nexti<=8 and 1<=nextj<=8): # 다음자리가 넘어가면 걍 버림.
        # print('건너뜀')
        continue
    if (nexti,nextj) == (si,sj):        # 갈자리에 돌잇으면 돌 옮기기
        # print('돌있음')
        si += mi
        sj += mj
        ni += mi
        nj += mj
        if not (1<=si<=8 and 1<=si<=8):     #만약에 돌이 넘어가면
            si -= mi                        #취소하고
            sj -= mj
            ni -= mi
            nj -= mj
            # print('건너뜀')
            continue                        # 다음 이동으로
    else:
        ni = nexti
        nj = nextj
#     print('킹', ni,nj)
#     print('돌', si,sj)
# print('answer')
print(f'{row[nj]}{ni}')
print(f'{row[sj]}{si}')
