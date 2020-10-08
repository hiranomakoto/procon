# atcoder 第11回日本情報オリンピック予選 D
# https://atcoder.jp/contests/joi2012yo/tasks/joi2012yo_d
# 動的計画法

n,k = map(int,input().split())

q = []
for _ in range(k):
    a,b = map(int,input().split())
    q.append((a,b))

q.sort(key=lambda x:x[0])
# 第一index：i日目まで計算した
# 第２、第３index：2日前、１日前にそれぞれ食べたパスタの種類
# 配列の中身は、何通り mod 10000
dp = [[[0 for _ in range(4)] for _ in range(4)] for _ in range(n+1)]
dp[0][1][2] = 1

for i in range(n):
    if q and q[0][0] == i+1:
        _,b = q.pop(0)
    else:
        b = 0
    for l in range(1,4):
        for m in range(1,4):
            if b and not m == b:
                dp[i+1][l][m] = 0
            else:
                for j in range(1,4):
                    if i > 1 and l == m == j:
                        continue
                    dp[i+1][l][m] += dp[i][j][l]
                    dp[i+1][l][m] %= 10000
                
#for i,p in enumerate(dp):
    #print('{}:{}'.format(i,p))
print(sum([sum(a) for a in dp[n]]) % 10000)

