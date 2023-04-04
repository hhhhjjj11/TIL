# 아이디어. 
# 4개의 구역 중 어디인지 찾은다음에
# ★다시 영점조정해서 옮긴다. (r,c를 바꿔주기.)
# 포함된 영역을 찾은다음 그거의 꼭짓점을 0,0으로 갖다 붙이는 것과 같음.


N, r, c = map(int,input().split())

ans = 0 
size = 2 ** N
while size > 1:
    #print('size',size)
    # 1구역
    if 0 <= r < size//2 and 0 <= c < size//2:
        pass
        #print('1', ans)
    # 2구역
    elif 0 <= r < size//2 and size//2 <= c:
        ans += (size//2)**2 * 1
        c -= size//2
        #print('2', ans)
    # 3구역
    elif size//2 <= r  and 0 <= c < size//2:
        ans += (size//2)**2 * 2
        r -= size//2
        #print('3', ans)
    # 4구역
    else:
        ans += (size//2)**2 * 3
        r -= size//2
        c -= size//2
        #print('4', ans)
    size//= 2

print(ans)

# Q.이분탐색으로 푸는것과 비교? 