// https://atcoder.jp/contests/abc184/tasks/abc184_d
// C++ならACする

#include <iostream>
#include <cstring>
#include <iomanip>
using namespace std;
template<class T> inline bool chmax(T& a, T b) { if (a < b) { a = b; return true; } return false; }
template<class T> inline bool chmin(T& a, T b) { if (a > b) { a = b; return true; } return false; }

int a,b,c;

double dp[101][101][101]
double rec(int i, int j, int k){
    if (i==100 || j==100 || k==100) return 0;
    if (dp[i][j][k] < 200) return dp[i][j][k];

    double ans=0;
    ans += (rec(i+1,j,k)+1)*i/(i+j+k)
    ans += (rec(i,j+1,k)+1)*j/(i+j+k)
    ans += (rec(i,j,k+1)+1)*k/(i+j+k)
    return dp[i][j][k] = ans
}

int main(){
    cin >> a >> b >> c;

    memset(dp,200,sizeof(dp))

    cout << rec(a,b,c) << endl;
}