# ABC C
# https://atcoder.jp/contests/abc183/tasks/abc183_c
# 単純に都市間のコストが決まっているので、全順列を求めた

import itertools

n,k = map(int,input().split())

costs = [[0] for _ in range(n+1)]

for i in range(1,n+1):
    t = map(int,input().split())
    costs[i] += t

ans = 0
for path in itertools.permutations(range(2,n+1),n-1):
    cost = 0
    pos = 1
    for i in path:
        cost += costs[pos][i]
        pos = i
    cost += costs[i][1]
    #print(path,cost)
    if cost == k:
        ans += 1

print(ans)
