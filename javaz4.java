import java.io.*;
import java.util.*;

public class Main {
    static List<Integer>[] g;
    static int[] tin, tout;
    static boolean[] used;
    static int timer = 0;

    static void dfs(int v) {
        used[v] = true;
        tin[v] = ++timer;
        for (int to : g[v]) if (!used[to]) dfs(to);
        tout[v] = ++timer;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        g = new ArrayList[n + 1];
        for (int i = 1; i <= n; i++) g[i] = new ArrayList<>();

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            g[u].add(v);
            g[v].add(u); // для ориентированного графа удалите эту строку
        }

        for (int i = 1; i <= n; i++) Collections.sort(g[i]);

        tin = new int[n + 1];
        tout = new int[n + 1];
        used = new boolean[n + 1];

        for (int v = 1; v <= n; v++) if (!used[v]) dfs(v);

        StringBuilder sb = new StringBuilder();
        for (int v = 1; v <= n; v++)
            sb.append(v).append(": ").append(tin[v]).append(" ").append(tout[v]).append('\n');
        System.out.print(sb);
    }
}
