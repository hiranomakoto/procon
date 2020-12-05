

import queue

h,w = map(int,input().split())


field=[]
for _ in range(h):
    p = list(map(int,input().split()))
    field.append(p[::])

print('hoge')

dx = [1,0,-1,0]
dy = [0,1,0,-1]
x = y = 0

checked = [[0 for _ in range(w)] for _ in range(h)]

open = queue.Queue()
open.put((x,y))


def is_valid(x,y):
    return x >= 0 and y >= 0 and x < w and y < h

cost = 0
while(True):
    q = queue.Queue()
    while(q):
        x,y = open.get()
        for n in range(4):
            nx = x + dx[n]
            ny = y + dy[n]
            if is_valid(nx,ny) and field[y][x] == 0 and checked[ny][nx] == 0:
                q.put((nx,ny))
                checked[ny][nx] = 1
    cost += 1
    open = q
    if checked[h-1][w-1] == 1:
        break

if w == h == 0:
    print(cost)
else:
    print(cost+1)

