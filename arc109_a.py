

a,b,x,y = map(int,input().split())

dp = [[100000 for _ in range(101)] for _ in range(2)]

dp[0][a] = 0

if a > b:
    step = -1
else:
    step = 1

for j in range(a,b+step,step):
    for i in range(2):
        if i == 0 and j > 0:
            dp[1][j-1] = min(dp[1][j-1], dp[0][j] + x)
            dp[0][j-1] = min(dp[0][j-1], dp[1][j-1] + x)
        if i == 1 and j < 100:
            dp[0][j+1] = min(dp[0][j+1], dp[1][j] + x)
            dp[1][j+1] = min(dp[1][j+1], dp[0][j+1] + x)
        dp[(i+1)%2][j] = min(dp[(i+1)%2][j], dp[i][j] + x)
        if 0 < j+step < 101:
            dp[i][j+step] = min(dp[i][j+step], dp[i][j] + y)
            
print(dp[1][b])
