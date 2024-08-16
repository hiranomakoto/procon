n,q = map(int,input().split())
S = [list(map(int,input().split())) for _ in range(q)]

follows = [['N' for i in range(n)] for j in range(n)]

for s in S:
    if s[0] == 1:
        follows[s[1]-1][s[2]-1] = 'Y'
    if s[0] == 2:
        for i in range(n):
            if follows[i][s[1]-1] == 'Y':
                follows[s[1]-1][i] = 'Y'
    if s[0] == 3:
        to_follow = []
        for i in range(n):
            if follows[s[1]-1][i] == 'Y':
                to_follow.append(i)
        for x in to_follow:
            for j in range(n):
                if follows[x][j] == 'Y' and j != (s[1]-1):
                    follows[s[1]-1][j] = 'Y'

for line in follows:
    print(''.join(line))


