X, Y = map(int,input().split())

Znow = (Y*100)//X

if Znow >= 99:
    print(-1)

else:
    answer = 0
    left = 1
    right = X

    while left<=right:
        mid = (left+right)//2
        if (Y+mid)*100 // (X+mid) == Znow:
            left = mid + 1
        else:                               # 값이 변한 경우
            answer = mid                    # 일단 정답후보로 걸어놓고 더 작아도 변하는지 찾아줘야댐
            right = mid - 1                 # 더 작아도 변하는지 확인하기 위해서 탐색을 계속해나가야함.   

    print(answer)

# 설명
# 전체 = X 승률 98 -> 이긴수 0..98X
# 승률 1.98X /2X = 99퍼 
# 따라서 승률에 관계없이 여태까지 한 판수만큼 이기면 승률은 무조건오름
# 따라서 1~X 범위에서 탐색해주면 된다.
