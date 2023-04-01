# 병합정렬 주요 메커니즘
# 분할: 원소하나일때까지 쪼개고
# 병합
# 둘중 하나가 동날때까지 양쪽에서 커서옮겨가며 비교하기 (이때 문제에 따라 비교조건 작성.)
    # 이때 temp에 넣어놨다가 왼쪽오른쪽 병합 마친 이후에 arr에 temp의 해당범위인덱스 복사
# 둘중하나 동나면 남은 쪽 temp에 이어붙이기
# temp를 원래꺼에 해당범위인덱스동안 복사
# 질문. 재귀말고 다른 방법 가능한가??

# 알고는있자.
# 인자를 받는방식이 두가지 있따. 
# 방법1 : (맨앞인덱스, 마지막인덱스)
# 방법2 : (맨앞인덱스, len(arr))
# +1 -1조금씩 바꿔가며 적용해준다.


def merge_sort(low,high):
    # 만약에 항 한개면 쪼갤필요 없고, 비교도 필요 없음. 리턴
    if low == high :
        return
    
    mid = (low + high) // 2

    merge_sort(low,mid)
    merge_sort(mid+1,high)

    temp = []

    cursor_L = low
    cursor_R = mid+1

    # 둘중하나가 동날때까지
    while cursor_L <= mid and cursor_R <= high:
        # 조건 병합
        if serials[cursor_L] <= serials[cursor_R]:
            temp.append(serials[cursor_L])
            cursor_L += 1
        else: 
            temp.append(serials[cursor_R])
            cursor_R += 1

    while cursor_L <= mid:
        temp.append(serials[cursor_L])
        cursor_L += 1
    while cursor_R <= high:
        temp.append(serials[cursor_R])
        cursor_R += 1

    for i in range(low,high+1):
        serials[i] = temp[i-low]

    

serials = [4,5,6,3,3,3,2,47,4,3,22,14]


merge_sort(0,len(serials)-1)

print('결과', serials)