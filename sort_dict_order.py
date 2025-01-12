n,m = map(int,input().split())
target = [input() for _ in range(n)]

target.sort()

print(target[m-1])