#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef pair<int, int> PLL;
typedef __int128 lll;

void solve() {
    int n;
    cin >> n;
    vector<int> a(n);
    for (int i = 0; i < n; i++)
        cin >> a[i];
    auto check = [&](int x) {
        set<int> w;
        for (int i = 0; i < n; i++) {
            int t = a[i];
            while ((t >= x || w.count(t)) && t > 0)
                t /= 2;
            w.insert(t);
        }
        return w.size() == x;
    };
    int l = 0, r = n;
    while (l < r) {
        int mid = (l + r + 1) / 2;
        if (check(mid))
            l = mid;
        else
            r = mid - 1;
    }
    cout << l << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int T = 1;
    cin >> T;
    while (T--) {
        solve();
    }
}