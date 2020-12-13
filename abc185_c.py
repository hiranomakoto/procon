# https://atcoder.jp/contests/abc185/tasks/abc185_c
# 切れ目の候補はn-1通りで、この中から11選んで切るので、
# n-1C11を求める問題
# 11! = 39916800なので事前に計算して使っている

n = int(input()) - 1

ans = 1
for i in range(11):
    ans *= (n-i)
    
print(ans // 39916800)

