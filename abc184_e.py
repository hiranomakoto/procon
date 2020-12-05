# TLEした

import sys

h,w = map(int,input().split())

INF = 10**12
alp = 'abcdefghijklmnopqrstuvwxyz.SG'

wall = '#' * (w+2)
map = [wall]
for _ in range(h):
    map.append('#' + input() + '#')
map.append(wall)

costs = [[INF for _ in range(w+2)] for _ in range(h+2)]

tel = {}
for char in alp:
    tel[char] = []

q = []
for i in range(1,h+1):
    for j in range(1,w+1):
        p = map[i][j]
        if p == 'S':
            costs[i][j] = 0
            q.append((i,j))
            continue
        if p == 'G':
            g = (i,j)
        if p == '#' or p == '.' or p == 'G':
            continue
        tel[p].append((i,j))

#print(q)

for i,j in q:
    p = map[i][j]
    cost = costs[i][j]
    for ni,nj in ([(i,j-1),(i,j+1),(i-1,j),(i+1,j)] + tel[p]):
        if map[ni][nj] == '#' or costs[ni][nj] < INF:
            continue
        costs[ni][nj] = cost + 1
        if map[ni][nj] == 'G':
            print(cost + 1)
            #print(costs)
            sys.exit()
        q.append((ni,nj))

print(-1)



