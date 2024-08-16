n = int(input())
A = [int(input()) for _ in range(n)]

members = [0 for _ in range(n+1)]
x = y = 0

for a in A:
    members[a] += 1

for i,num in enumerate(members[1:]):
    if num == 2:
        y = i + 1
    if num == 0:
        x = i + 1


if x == 0:
    print('Correct')
else:
    print(y,x)
