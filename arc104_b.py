# AtCoder Regular Contest 104 問題A
# https://atcoder.jp/contests/arc104/tasks/arc104_b
# 条件を、「対象となる部分文字列に含まれる'A'と'T', 'C'と'G'が同数」と読み替え
# 毎回t.count()してしまうとTLEしたので、部分和的なlistを用意した


ns,s = input().split()
n = int(ns)

count = {
    'A': [0 for _ in range(n+1)],
    'T': [0 for _ in range(n+1)],
    'C': [0 for _ in range(n+1)],
    'G': [0 for _ in range(n+1)],
}

for i in range(1,n+1):
    for c in count.keys():
        count[c][i] = count[c][i-1]
    c = s[i-1]
    count[c][i] += 1

def get_count(c,i,j):
    return count[c][j] - count[c][i]

ans = 0
for i in range(n):
    for j in range(2,n-i+1,2):
        t = s[i:i+j]
        if(get_count('A',i,i+j) == get_count('T',i,i+j) and get_count('C',i,i+j) == get_count('G',i,i+j)):
            ans += 1
        
print(ans)
