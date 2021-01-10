# https://atcoder.jp/contests/abc188/tasks/abc188_d
# 一日ごとに計算すると間に合わないので、コストの変化するポイントだけを計算する
# コストの変化するポイントは高々10^5なので間に合う

N,C = map(int,input().split())

sche = {}
milestone = []

for _ in range(N):
    a,b,c = map(int,input().split())
    milestone.append(a)
    # b日まで使うので、費用が変わるのはb+1日から
    milestone.append(b + 1)
    if a in sche.keys():
        sche[a] += c
    else:
        sche[a] = c
    if b + 1 in sche.keys():
        sche[b + 1] -= c
    else:
        sche[b + 1] = -c

milestone = list(set(milestone))
milestone.sort()

ans = 0
cost = 0
for i in range(len(milestone)-1):
    cost += sche[milestone[i]]
    ans += max(0, min(C, cost)) * (milestone[i+1] - milestone[i]) 

print(ans)
