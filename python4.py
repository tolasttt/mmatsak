import sys
sys.setrecursionlimit(1_000_000)

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it))

    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        g[u].append(v)
        g[v].append(u)  # для ориентированного графа удалите эту строку

    for v in range(1, n + 1):
        g[v].sort()

    tin = [0] * (n + 1)
    tout = [0] * (n + 1)
    used = [False] * (n + 1)
    timer = 0

    def dfs(v):
        nonlocal timer
        used[v] = True
        timer += 1; tin[v] = timer
        for to in g[v]:
            if not used[to]:
                dfs(to)
        timer += 1; tout[v] = timer

    for v in range(1, n + 1):
        if not used[v]:
            dfs(v)

    print("\n".join(f"{v}: {tin[v]} {tout[v]}" for v in range(1, n + 1)))

if __name__ == "__main__":
    main()
