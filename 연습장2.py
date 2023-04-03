from collections import deque
N, r, c = map(int,input().split())

# 아이디어: 행과 열을 가지고 '오/왼', '위/아래'를 나눈다.


j_left = 0
j_right = 2**N -1   
i_left = 0
i_right = 2**N -1
recordI = deque()
recordJ = deque()

while i_left <= i_right :
    middle = (i_left+i_right)//2

    if r == middle:
        break
    elif middle <= r:
        i_left = middle+1
        recordI.append('D')
    else:
        i_right = middle
        recordI.append('U')

while j_left <= j_right :
    middle = (j_left+j_right)//2

    if c == middle:
        #print('c==middle')
        break
    elif middle <= c:
        j_left = middle+1
        recordJ.append('L') 
    else:
        j_right = middle
        recordJ.append('R')


print(recordI)
print(recordJ)

res = 0
boxsize = 2*(N-1)

while True:
    print('res',res)
    print('boxsize', boxsize)
    if recordI and recordJ:
        I = recordI.popleft()
        J = recordJ.popleft()
        if (I,J) == ('U','L'):
            pass
        elif (I,J) == ('D','R'):
            res += boxsize**2 * 3
        elif (I,J) == ('U','R'):
            res += boxsize**2 * 1
        elif (I,J) == ('D','L'):
            res += boxsize**2 * 2
    elif recordI and not recordJ:
        I = recordI.popleft()
        # 없다는건 middle = c 이고, middle 은 왼쪽에 속함.
        if I == 'U': # 'U','L' 즉 1번박스
            pass
        elif I == 'D':
            res += boxsize**2 * 2
    elif not recordI and recordJ:
        J = recordJ.popleft()
        # 없다는건 middle = r 이고, middle 은 위에 속함.
        if J == 'R':
            res += boxsize**2 * 1
        elif J == 'L':
            pass
    else:
        # 무조건 4번임
        res += boxsize**2 *4
        break
    boxsize //= 2


print(res-1)

# 1 1 1 1 
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1 