# ARC C
# https://atcoder.jp/contests/arc106/tasks/arc106_c

n,m = map(int,input().split())

# mが負、mが正かつ m >= n-1 はありえない
if m < 0 or (m > 0 and m > n - 2):
    print(-1)
# n = 1 , m = 0の場合
elif n == 1 and m == 0:
    print(1,2)
# m >= 0, n >= 2の場合
else:
    i = 1
    # m+1個の非連結区間
    for _ in range(m+1):
        print(2*i, 2*i+1)
        i += 1
    # 一つの大きな区間で囲む
    print(1,2*i)
    i += 1
    # 残りを非連結な区間とする
    for _ in range(n-m-2):
        print(2*i,2*i+1)
        i += 1
