# ARC C
# https://atcoder.jp/contests/arc107/tasks/arc107_c
# WAが3件出る。もう一息

n,k = map(int,input().split())

mat = []
for _ in range(n):
    mat.append(list(map(int,input().split())))

lines = []
columns = []
for i in range(n-1):
    for j in range(i+1,n):
        flg_l = False
        flg_c = False
        for h in range(n):
            if mat[i][h] + mat[j][h] > k:
                flg_l = True
            if mat[h][i] + mat[h][j] > k:
                flg_c = True
            if flg_l and flg_c:
                break
        if not flg_l:
            lines.append(i)
            lines.append(j)
        if not flg_c:
            columns.append(i)
            columns.append(j)
MOD = 998244353
count_l = 1
count_c = 1

for i in range(1,len(set(lines))+1):
    count_l = count_l * i % MOD

for i in range(1,len(set(columns))+1):
    count_c = count_c * i % MOD

print(count_l * count_c % MOD)

