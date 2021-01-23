# https://atcoder.jp/contests/abc189/tasks/abc189_e
# 各オペレーションがアフィン変換なので、オペレーションの累積積を求めておけば
# 各クエリの解がO(1)で求まる
# 楽しようとnumpyを使ったらTLEになった

import numpy as np

def ope1(prev):
    return np.dot(np.array([[0,1,0],[-1,0,0],[0,0,1]]), prev)

def ope2(prev):
    return np.dot(np.array([[0,-1,0],[1,0,0],[0,0,1]]), prev)

def ope3(prev,p):
    return np.dot(np.array([[-1,0,2*p],[0,1,0],[0,0,1]]), prev)

def ope4(prev,p):
    return np.dot(np.array([[1,0,0],[0,-1,2*p],[0,0,1]]), prev)

n = int(input())

unit = []
for _ in range(n):
    x,y = map(int,input().split())
    unit.append(np.array([x,y,1]))

m = int(input())

opes = [np.array([[1,0,0],[0,1,0],[0,0,1]])]

for _ in range(m):
    o = list(map(int,input().split()))
    prev = opes[-1]
    if o[0] == 1:
        opes.append(ope1(prev))
    elif o[0] == 2:
        opes.append(ope2(prev))
    elif o[0] == 3:
        opes.append(ope3(prev, o[1]))
    else:
        opes.append(ope4(prev, o[1]))

q = int(input())

for _ in range(q):
    a,b = map(int,input().split())
    x,y,_ = np.dot(opes[a],unit[b-1])
    print(x,y)
