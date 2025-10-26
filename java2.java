public class FibSearch {

    public static int fibonacci(int[] a, int x) {
        int n = a.length;
        int f2 = 0, f1 = 1, f = f1 + f2;
        while (f < n) { f2 = f1; f1 = f; f = f1 + f2; }
        int offset = -1;
        while (f > 1) {
            int i = Math.min(offset + f2, n - 1);
            if (a[i] < x) {
                f = f1;
                f1 = f2;
                f2 = f - f1;
                offset = i;
            } else if (a[i] > x) {
                f = f2;
                f1 = f1 - f2;
                f2 = f - f1;
            } else return i;
        }
        if (f1 == 1 && offset + 1 < n && a[offset + 1] == x) return offset + 1;
        return -1;
    }

    public static void main(String[] args) {
        int[] sorted = {10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100};
        int key = 85;
        int idx = fibonacci(sorted, key);
        if (idx != -1) System.out.println("Элемент " + key + " найден на индексе " + idx);
        else System.out.println("Элемент " + key + " не найден в массиве.");
    }
}