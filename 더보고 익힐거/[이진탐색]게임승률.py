# 이진탐색

# 핵심1 : 문제마다 탐색범위를 잘 생각해서 정해주어야한다는 점.
    # 설명
    # 전체 = X 승률 98 -> 이긴수 0..98X
    # 승률 1.98X /2X = 99퍼
    # 따라서 승률에 관계없이 여태까지 한 판수만큼 이기면 승률은 무조건오름
    # 따라서 1~X 범위에서 탐색해주면 된다.

# 핵심2 : 문제마다

X, Y = map(int,input().split())

Znow = (Y*100)//X

if Znow >= 99:
    print(-1)
else:
    answer = 0
    left = 1
    right = X

    while left <= right:
        mid = (left + right)//2
        if (Y+mid)*100 // (X+mid) == Znow:
            left = mid + 1
        else:                           # 값이 변한 경우
            answer = mid                # 일단 정답후보로 걸어놓고 더 작아도 변하는지 찾아줘야댐
            right = mid - 1             # 더 작아도 변하는지 확인하기 위해서 탐색을 계속해나가야함.

    print(answer)

# 오류코드2
# 이유 : 시간초과.
# 참고 : 부동소수점 오류?? 때문에 int만든다음에 100곱하는 식으로 하면 값이 틀림. (ㅅㅂ생각해보니 당연히 안되지)
# X, Y = map(int,input().split())

# Znow = (Y*100)//X

# cnt = 0

# if Znow >= 99:
#     if Znow == 99:
#         print(-1)
#     else:
#         print(1)
# else:
#     while True:
#         Z = ((Y+cnt)*100)//(X+cnt)
#         if Znow != Z:
#             break
#         cnt += 1
#     print(cnt)