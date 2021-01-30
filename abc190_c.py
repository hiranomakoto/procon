# https://atcoder.jp/contests/abc190/tasks/abc190_c
# bit全検索

n,m = map(int,input().split())
cond = [list(map(int,input().split())) for _ in range(m)]

k = int(input())
players = [list(map(int,input().split())) for _ in range(k)]

#print(cond)
#print(players)

ans = 0
for i in range(2 ** k):
    #print(bin(i))
    dishes = [0 for _ in range(n)]
    for j in range(k):
        if i % 2 == 0:
            dishes[players[j][0]-1] = 1
        else:
            dishes[players[j][1]-1] = 1
        i //= 2
    count = 0
    for j in range(m):
        if dishes[cond[j][0]-1] and dishes[cond[j][1]-1]:
            count += 1
    ans = max(ans,count)

print(ans)
