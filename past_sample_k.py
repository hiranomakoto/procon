n = int(input())
p = [(int(input())-1) for _ in range(n)]
q = int(input())
queries = [list(map(lambda x:int(x)-1,input().split())) for _ in range(q)]

t = [[] for _ in range(n)]

for i in range(n):
    parent = p[i]
    if parent == -2:
        root = i
    else:
        t[parent].append(i)

sub_t = [[0,0] for _ in range(n)]
search_order = 0

def rec(i:int):
    global search_order
    sub_t[i][0] = search_order
    search_order += 1
    for child in t[i]:
        rec(child)
    sub_t[i][1] = search_order

rec(root)

for a,b in queries:
    if sub_t[b][0] < sub_t[a][0] and sub_t[b][1] > sub_t[a][0]:
        print('Yes')
    else:
        print('No')

