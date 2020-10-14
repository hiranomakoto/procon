# AOJ Project Management
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2503
# メモ化再帰

n,m = map(int, input().split())

G = [[] for _ in range(n)]
dp = [-1] * n

for _ in range(m):
    a,b,c = map(int, input().split())
    G[a].append((b,c))

def rec(v):
    if dp[v] > -1:
        return dp[v]
    
    cost = 0
    for nv in G[v]:
        cost = max(cost, rec(nv[0]) + nv[1])
    
    dp[v] = cost
    
    return cost

rec(0)
print(dp[0])

