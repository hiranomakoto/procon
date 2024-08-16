n = int(input())
C = list(map(int,input().split()))
q = int(input())
S = [list(map(int,input().split())) for _ in range(q)]

all_min = min(C)
odd_min = min(C[::2])
all_sold = 0
odd_sold = 0
solo_sold = 0

for s in S:
    if s[0] == 1:
        if s[1] % 2 == 0 and C[s[1]-1] - all_sold < s[2]:
            continue
        if s[1] % 2 == 1 and C[s[1]-1] - all_sold - odd_sold < s[2]:
            continue
        C[s[1]-1] -= s[2]
        solo_sold += s[2]
        all_min = min(all_min, C[s[1]-1])
        if s[1] % 2 == 1:
            odd_min = min(odd_min, C[s[1]-1])
    if s[0] == 2 and odd_min >= s[1]:
        odd_sold += s[1]
        odd_min -= s[1]
        all_min = min(all_min, odd_min)
    if s[0] == 3 and all_min >= s[1]:
        all_sold += s[1]
        all_min -= s[1]
        odd_min -= s[1]

sold = solo_sold
sold += all_sold * n
sold += odd_sold * (n // 2 + n % 2)

print(sold)
