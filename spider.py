# AOJ スパイダー人
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0155
# 動的計画法＋復元

import math

# 平方根をとるのが大変なので、距離の二乗で処理する
reach = 50
INF = 10 ** 12

def get_distances(n,buildings):
    global reach
    
    # 添え字はビル番号
    distances = [[INF for _ in range(n+1)] for _ in range(n+1)]
    buildings.sort(key=lambda x:x[0])
    for i,b in enumerate(buildings):
        for j in range(i):
            b_t = buildings[j]
            d = math.sqrt((b[1] - b_t[1]) ** 2 + (b[2] - b_t[2]) ** 2)
            if d <= reach:
                distances[b[0]][b_t[0]] = d
                distances[b_t[0]][b[0]] = d
    return distances

def get_route(n, distances, s, g):
    # dp[i+1][j] : iホップホップで考慮した時のbuild[s]からbuild[j]までの最短距離
    # build番号が1オリジンなので、n+2まで考慮
    dp = [[INF for _ in range(n+2)] for _ in range(n+1)]
    # route[i][j] : iホップホップで考慮した時のbuild[s]からbuild[j]までの最短距離
    # をたどるときの経路
    route = [['' for _ in range(n+2)] for _ in range(n+2)]
    dp[0][s] = 0
    route[0][s] = str(s)
    for i in range(n):
        for j in range(1,n+1):
            dp[i+1][j] = dp[i][j]
            route[i+1][j] = route[i][j]
            for k in range(1,n+1):
                if k == j:
                    continue
                if distances[j][k] < INF:
                    if dp[i+1][j] > dp[i][k] + distances[j][k]:
                        route[i+1][j] = route[i][k] + ' ' + str(j)
                        dp[i+1][j] = dp[i][k] + distances[j][k]
    if route[n][g]:
        return route[n][g]
    else:
        return 'NA'
    """
    for p in dp:
        print(p)
    print()
    for p in route:
        print(p)
    return dp
    """

while(True):
    n = int(input())
    if n == 0:
        break

    buildings = []
    for _ in range(n):
        b, x, y = map(int,input().split())
        buildings.append((b,x,y))
    
    distances = get_distances(n,buildings)
    #print(distances)
    
    m = int(input())
    for _ in range(m):
        s,g = map(int,input().split())
        ret = get_route(n, distances, s, g)
        print(ret)
    
