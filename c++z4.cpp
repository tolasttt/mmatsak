#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    if (!(cin >> n >> m)) return 0;

    vector<vector<int>> g(n + 1);
    for (int i = 0; i < m; ++i) {
        int u, v; cin >> u >> v;
        g[u].push_back(v);
        g[v].push_back(u); // для ориентированного графа удалите эту строку
    }

    for (int v = 1; v <= n; ++v) sort(g[v].begin(), g[v].end());

    vector<int> tin(n + 1), tout(n + 1);
    vector<char> used(n + 1, 0);
    int timer = 0;

    function<void(int)> dfs = [&](int v) {
        used[v] = 1;
        tin[v] = ++timer;
        for (int to : g[v]) if (!used[to]) dfs(to);
        tout[v] = ++timer;
    };

    for (int v = 1; v <= n; ++v) if (!used[v]) dfs(v);

    for (int v = 1; v <= n; ++v)
        cout << v << ": " << tin[v] << " " << tout[v] << "\n";
}
