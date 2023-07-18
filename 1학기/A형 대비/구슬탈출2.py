from pprint import pprint

N,M = map(int,input().split())

def right(Xi,Xj):
    RB = 'R' if brd[Xi][Xj]=='R' else 'B' 
    brd[Xi][Xj] = '.'
    cnt = 0
    temp = []
    while brd[Xi][Xj-cnt-1] != '#':
        temp.append(brd[Xi][Xj-cnt-1])
        cnt +=1
    #print('temp is',temp)
    #print('cnt is',cnt)
    if 'B' in temp or 'R' in temp:
        #print('딴색공앞에걸림')
        Xj -= (cnt-1)
    else:
        Xj -= cnt
    brd[Xi][Xj] = 'R' if RB =='R' else 'B'
    return Xi,Xj


def left(Xi,Xj):
    RB = 'R' if brd[Xi][Xj]=='R' else 'B' 
    brd[Xi][Xj] = '.'
    cnt = 0
    temp = []
    while brd[Xi][Xj-cnt-1] != '#':
        temp.append(brd[Xi][Xj-cnt-1])
        cnt +=1
    #print('temp is',temp)
    #print('cnt is',cnt)
    if 'B' in temp or 'R' in temp:
        #print('딴색공앞에걸림')
        Xj -= (cnt-1)
    else:
        Xj -= cnt
    brd[Xi][Xj] = 'R' if RB =='R' else 'B'
    return Xi,Xj

def up():
    pass

def down():
    pass



brd = [list(input()) for i in range(N)]

for i in range(1,N-1):
    for j in range(1,M-1):
        if brd[i][j] == 'R':
            Ri,Rj = i,j
        elif brd[i][j] == 'B':
            Bi,Bj = i,j
        elif brd[i][j] == 'O':
            Oi,Oj = i,j

# print(Ri,Rj)
# print(Bi,Bj)
# print(Oi,Oj)
left(Ri,Rj)
print('board')
for i in brd:
    print(''.join(i))

left(Bi,Bj)
print('board')
for i in brd:
    print(''.join(i))
#pprint(brd)
cnt = 1

Adj = [(1,0),(-1,0),(0,1),(0,-1)]

