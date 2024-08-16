
def calc_teamscore(team:list):
    if len(team) < 2:
        return 0
    teamscore = 0
    for i in range(len(team)):
        for j in range(i):
            teamscore += a[team[i]][team[j]]
    return teamscore


def calc_score(gr:int):
    teams = [[] for _ in range(3)]
    for i in range(n):
        team = gr // (3 ** (n-i-1))
        teams[team].append(i)
        gr %= 3 ** (n-i-1)
    teamscore = 0
    for i in range(3):
        teamscore += calc_teamscore(teams[i])
    return teamscore

n = int(input())
a = [list(map(int,input().split())) for _ in range(n-1)]
a.append([0])
for i in range(n):
    a[i] = [0] * (i+1) + a[i]

for i in range(n):
    for j in range(i):
        a[i][j] = a[j][i]

score = -1000000 * n -1
for i in range(3 ** n):
    score = max(score , calc_score(i))

print(score)

