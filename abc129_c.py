# abc129_c

n,m = map(int,input().split())

l = []

for _ in range(m):
    a = int(input())
    l.append(a)

dp = [0 for _ in range(n+1)]
dp[0] = 1

for i in range(1, n + 1):
    if l and i == l[0]:
        l.pop(0)
        continue
    if i == 1:
        dp[i] = dp[i-1]
    else:
        dp[i] = max(dp[i], dp[i-1] + dp[i-2]) % 1000000007
        if(dp[i] == 0 and dp[i-1] == 0):
            break
print(dp[n])
