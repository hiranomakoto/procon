n,m = map(int,input().split())

def bitnize(s:str)->int:
    retval = 0
    for i,part in enumerate(s):
        if part == 'Y':
            retval += 2**i
    return retval

sets = []
for _ in range(m):
    s = input().split()
    sets.append((bitnize(s[0]), int(s[1])))

INF = 10 ** 12

dp = [[INF for i in range(2 ** n)] for j in range(m+1)]

for i in range(m):
    dp[i][0] = 0
    for j in range(2 ** n):
        dp[i+1][j] = min(dp[i][j], dp[i+1][j])
        dp[i+1][j | sets[i][0]] = min(dp[i+1][j | sets[i][0]], dp[i][j | sets[i][0]], dp[i][j] + sets[i][1])

ans = dp[m][2 ** n - 1]
if ans == INF:
    print(-1)
else:
    print(ans)


