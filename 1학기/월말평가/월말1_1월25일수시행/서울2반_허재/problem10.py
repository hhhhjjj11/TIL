# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def is_position_safe(N, M, position):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    """
    입력 position 으로부터 현재 위치 i,j를 얻는다.
    M=0,1,2,3은 각각 위로, 아래로, 좌로, 우로 한칸씩 이동하는 것이므로
    이는 i와 j를 각각 1씩 더하거나 빼는것과 같다.
    M에 따라 i와 j를 재할당 한 후에 현재 위치(i,j)가 범위(0,0)~(N-1,N-1)를 벗어나는지 판별한다.
    """
    i,j=position
    M=int(M)
    N=int(N)

    if M == 0 :  # 위로감. 행하나 줄어듬
        i-=1
    elif M == 1:
        i+=1
    elif M == 2:
        j-=1
    elif M == 3:
        j+=1

    if 0<=i<=N-1 and 0<=j<=N-1:
        return True
    else:
        return False

# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
########## 코드 변경 금지 ############
if __name__ == '__main__':
    print(is_position_safe(3, 1, (0, 0)))  # True
    print(is_position_safe(3, 0, (0, 0)))  # False
