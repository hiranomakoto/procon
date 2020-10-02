# AOJ168
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0168
# 動的計画法

def judge(n):
    dp = [0 for _ in range(n+1)]
    dp[0] = dp[1] = 1
    for i in range(1,n+1):
        if i == 2:
            dp[2] = 2
        else:
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return(dp[n]//3650 + 1)

while(True):
    n = int(input())
    if(n==0):
        break
    else:
        print(judge(n))

