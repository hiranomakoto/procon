# abc180 D
# https://atcoder.jp/contests/abc180/tasks/abc180_d
# 動的計画法っぽいので動的計画法で解こうとするとTLEする

x,y,a,b = map(int,input().split())

ex = 0
while(x < (b / (a-1)) and x < y/a):
    ex += 1
    x *= a

ex += (y-x-1)//b
print(max(ex,0))

