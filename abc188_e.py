# https://atcoder.jp/contests/abc188/tasks/abc188_e
# 動的計画法

N,M = map(int,input().split())
A = list(map(int,input().split()))
path = [[] for _ in range(N)]

for _ in range(M):
    x,y = map(int,input().split())
    path[x-1].append(y-1)

# その町にたどり着くまでの金の最安値
dp = A[::]

ans = -1000000000
for i in range(N):
    for n in path[i]:
        dp[n] = min(dp[n],dp[i])
        ans = max(ans,A[n] - dp[i])

print(ans)

