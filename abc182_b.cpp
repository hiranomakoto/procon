# ABC182 B
# https://atcoder.jp/contests/abc182/tasks/abc182_b
# 共通の因数の最大値

#include <iostream>
#include <vector>
using namespace std;
int main(void){
    // Your code here!
    
    int n;
    cin >> n;

    vector<int> a(n);
    for(int i=0;i<n;++i) cin >> a[i];

    vector<int> count(1001);
    int ans=2;
    
    for(int i : a){
        for(int j=1; j*j<=i; ++j){
            if(i%j==0){
                count[j]++;
                if(j*j!=i) count[int(i/j)]++;
            }
        }
    }
    for(int i=2;i<1000;++i){
        if(count[ans] < count[i]) ans = i;
    }
    cout << ans << endl;
}
