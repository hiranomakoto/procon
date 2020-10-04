# AtCoder Regular Contest 104 問題A
# https://atcoder.jp/contests/arc104/tasks/arc104_a
# 方程式を解いて計算式にした


a,b = map(int,input().split())

x = (a+b) // 2
y = (a-b) // 2

print('{} {}'.format(x,y))
