# Indeedなう C
# https://atcoder.jp/contests/indeednow-finala-open/tasks/indeednow_2015_finala_c
# 動的計画法

n,m = map(int,input().split())

companies = []
for _ in range(n):
    a,b,c,w = map(int,input().split())
    companies.append((a,b,c,w))

candidates = []
for _ in range(m):
    a,b,c = map(int,input().split())
    candidates.append((a,b,c))

heatmap = [[[0 for _ in range(101)] for _ in range(101)] for _ in range(101)]

for c in companies:
    heatmap[c[0]][c[1]][c[2]] = max(heatmap[c[0]][c[1]][c[2]], c[3])

# 各軸
for i in range(1,101):
    heatmap[i][0][0] = max(heatmap[i][0][0], heatmap[i-1][0][0])
    heatmap[0][i][0] = max(heatmap[0][i][0], heatmap[0][i-1][0])
    heatmap[0][0][i] = max(heatmap[0][0][i], heatmap[0][0][i-1])

# 各面
for i in range(1,101):
    for j in range(1,101):
        heatmap[i][j][0] = max(heatmap[i][j][0], heatmap[i-1][j][0], heatmap[i][j-1][0])
        heatmap[i][0][j] = max(heatmap[i][0][j], heatmap[i-1][0][j], heatmap[i][0][j-1])
        heatmap[0][i][j] = max(heatmap[0][i][j], heatmap[0][i-1][j], heatmap[0][i][j-1])

# 空間
for i in range(1,101):
    for j in range(1,101):
        for k in range(1,101):
            heatmap[i][j][k] = max(heatmap[i][j][k], heatmap[i-1][j][k],
                                    heatmap[i][j-1][k], heatmap[i][j][k-1])

# 回答
for c in candidates:
    print(heatmap[c[0]][c[1]][c[2]])
