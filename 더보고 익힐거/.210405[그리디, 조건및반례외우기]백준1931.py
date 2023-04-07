# 주의: x[1],x[0] 까지 정렬 해줘야함
# 끝나는 시간이 같을 경우 시작시간순으로 정렬 해줘야 함!
# 반례)
# [(1,5),()]

N = int(input())

li = [list(map(int,input().split())) for _ in range(N)]

li.sort(key = lambda x : (x[1],x[0])) # 끝나는 시간 기준 정렬 

t_now = 0
END = li[-1][1]
cnt = 0
for i in range(N):
    s, e = li[i]
    if s >= t_now:
        t_now = e
        cnt += 1
    
print(cnt)

    