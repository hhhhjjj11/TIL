# 아이디어 외워.
# 이전의 연결된 두 항 중 큰 값을 취한다..
# 뭔가 순차적으로 생각하는것이 아니라
# 뒤에서 부터 생각하는 듯하다.

# 다음항에서, 앞의 두개 중 뭘 받을지 고른다....
# 이전항에서 두개 중 뭐로 갈지가 아니라.

n = int(input())
dp = [list(map(int,input().split())) for _ in range(n)]

 
for i in range(1,n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] += dp[i-1][j]            
        elif j == i:
            dp[i][j] += dp[i-1][j-1]
        else:
            dp[i][j] += max(dp[i-1][j],dp[i-1][j-1])

print(max(dp[n-1]))
