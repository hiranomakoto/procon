# https://atcoder.jp/contests/abc184/tasks/abc184_d
# pypy3ではTLEしてしまう

a,b,c = map(int,input().split())

dp = [[[200 for _ in range(101)] for _ in range(101)] for _ in range(101)]

def rec(i,j,k):
    if i==100 or j==100 or k==100:
        return 0
    if dp[i][j][k] < 200:
        return dp[i][j][k]
    
    dp[i][j][k] = i/(i+j+k)*(rec(i+1,j,k) + 1) +\
            j/(i+j+k)*(rec(i,j+1,k) + 1) +\
            k/(i+j+k)*(rec(i,j,k+1) + 1)
    return dp[i][j][k]

print(rec(a,b,c))


