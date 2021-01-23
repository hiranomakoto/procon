# https://atcoder.jp/contests/abc189/tasks/abc189_c
# l,rの全検索になる
# [l,r)区間の最小値を求めるのにうっかりセグメント木とか使うとTLEする
# 素直に頭から更新すればよい。

n = int(input())
a = list(map(int,input().split()))

ans = 0
for l in range(n):
    x = a[l]
    for r in range(l,n):
        x = min(x,a[r])
        ans = max(ans,x * (r-l+1))

print(ans)
