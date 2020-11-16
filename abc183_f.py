# ABC183 F
# https://atcoder.jp/contests/abc183/tasks/abc183_f
# UnionFind木をちょっと変更

from collections import defaultdict

class MyUnionFind:
    # 作りたい要素数nで初期化
    # 使用するインスタンス変数の初期化
    def __init__(self, n, cls_idx):
        self.n = n
        # root[x]<0ならそのノードが根かつその値が木の要素数
        # rootノードでその木の要素数を記録する
        self.root = [-1]*(n+1)
        # 木をくっつける時にアンバランスにならないように調整する
        self.rank = [0]*(n+1)
        
        self.cls_idx = cls_idx

    # ノードxのrootノードを見つける
    def findRoot(self, x):
        if(self.root[x] < 0): # 根
            return x
        else:
            # ここで代入しておくことで、後の繰り返しを避ける
            self.root[x] = self.findRoot(self.root[x])

            for i in self.cls_idx[x].keys():
                self.cls_idx[-self.root[x]][i] += self.cls_idx[x][i]
                self.cls_idx[x][i] = 0

            return self.root[x]
    # 木の併合、入力は併合したい各ノード
    def unite(self, x, y):
        # 入力ノードのrootノードを見つける
        x = self.findRoot(x)
        y = self.findRoot(y)
        # すでに同じ木に属していた場合
        if x == y:
            return
        # 違う木に属していた場合rankを見てくっつける方を決める
        if self.rank[x] > self.rank[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
            
            for i in self.cls_idx[y].keys():
                self.cls_idx[x][i] += self.cls_idx[y][i]
                self.cls_idx[y][i] = 0

        else:
            self.root[y] += self.root[x]
            self.root[x] = y

            for i in self.cls_idx[x].keys():
                self.cls_idx[y][i] += self.cls_idx[x][i]
                self.cls_idx[x][i] = 0

            # rnkが同じ（深さに差がない場合）は1増やす
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    # xとyが同じグループに属するか判断
    def isSameGroup(self, x, y):
        return self.findRoot(x) == self.findRoot(y)

    # ノードxが属する木のサイズを返す
    def count(self, x):
        return -self.root[self.findRoot(x)]


n,q = map(int,input().split())

cls_idx = [defaultdict(int) for _ in range(n+1)]

cs = map(int,input().split())

for i,c in enumerate(cs):
    cls_idx[i+1][c] = 1

t = MyUnionFind(n+1,cls_idx)

for _ in range(q):
    k,a,b = map(int,input().split())
    if k == 1:
        t.unite(a,b)
    else:
        r = t.findRoot(a)
        print(cls_idx[r][b])
