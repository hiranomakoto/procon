# ABC182 E
# https://atcoder.jp/contests/abc182/tasks/abc182_e
# 縦と横を独立で考える

h,w,n,m = map(int,input().split())

map1 = [[0 for _ in range(w+1)] for _ in range(h+1)]
map2 = [[0 for _ in range(w+1)] for _ in range(h+1)]

for _ in range(n):
    a,b = map(int,input().split())
    map1[a][b] = 1

for _ in range(m):
    a,b = map(int,input().split())
    map1[a][b] = 2

def turn_on_h(y,start,end):
    for x in range(start,end):
        map2[y][x] = 1

def turn_on_v(x,start,end):
    for y in range(start,end):
        map2[y][x] = 1

for y in range(h+1):
    start = 1
    light = False
    for x in range(w+1):
        c = map1[y][x]
        if c == 1:
            light = True
        elif c == 2:
            if light:
                turn_on_h(y,start,x)
            start = x+1
            light = False
    if light:
        turn_on_h(y,start,x+1)

for x in range(w+1):
    start = 1
    light = False
    for y in range(h+1):
        c = map1[y][x]
        if c == 1:
            light = True
        elif c == 2:
            if light:
                turn_on_v(x,start,y)
            start = y+1
            light = False
    if light:
        turn_on_v(x,start,y+1)
"""
for p in map1:
    print(p)
print()
"""
ans = 0
for p in map2:
    ans += sum(p)
print(ans)
