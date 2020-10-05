# abc015 d
# https://atcoder.jp/contests/abc015/tasks/abc015_4
# 動的計画法

w_total = int(input())
n,k = map(int, input().split())

w_l = [0 for _ in range(n)]
v_l = [0 for _ in range(n)]

for i in range(n):
    a,b = map(int,input().split())
    w_l[i] = a
    v_l[i] = b

dp = [[0 for _ in range(w_total + 1)] for _ in range(k+1)]
next_hop = [[0 for _ in range(w_total + 1)] for _ in range(k+1)]

for i in range(n):
    for j in range(i+1):
        if j >= k:
            break
        for weight_s in range(w_total+1):
            if w_l[i] <= weight_s:
                next_hop[j+1][weight_s] = max(next_hop[j+1][weight_s], dp[j][weight_s - w_l[i]] + v_l[i])
            next_hop[j+1][weight_s] = max(next_hop[j+1][weight_s], dp[j][weight_s])
    dp = [x[:] for x in next_hop]
    #print('{}:'.format(i))
    #for p in dp:
        #print(p)

print(dp[k][w_total])

