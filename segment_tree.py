# RMQ
# update(i,x): i 番目の要素を x に更新。O(log(n))
# query(a,b): [a,b) での最小の要素を取得。O(log(n))

class segmetTree(object):
    def __init__(self,n,func,NA):
        """
        n:要素の個数
        func:評価関数
        NA:パディングする値
        """
        self.NA = NA
        x = 1
        while(n>x):
            x *= 2
        self.n = x
        self.dat = [self.NA for _ in range(2*x)]
        self.func = func
    
    def update(self,i,x):
        i += (self.n - 1)
        self.dat[i] = x
        while(i > 0):
            # 親を順次更新
            i = (i - 1) // 2
            self.dat[i] = self.func(self.dat[i * 2 + 1], self.dat[i * 2 + 2])
    
    def query_sub(self,a,b,k,l,r):
        if r <= a or b <= l:
            return self.NA
        elif a <= l and r <= b:
            return self.dat[k]
        else:
            vl = self.query_sub(a, b, k * 2 + 1, l, (l + r) // 2)
            vr = self.query_sub(a, b, k * 2 + 2, (l + r) // 2, r)
            return self.func(vl, vr)
    
    def query(self,a,b):
        return self.query_sub(a,b,0,0,self.n)



t = segmetTree(10)
for i in range(10):
    t.update(i,(i * i) % 7)

print(t.query(7,10))
print(t.dat)



