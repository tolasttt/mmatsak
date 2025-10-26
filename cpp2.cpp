#include <iostream>
#include <vector>
#include <algorithm>

static void dump(const std::vector<int>& v, const std::string& tag = {}) {
    if (!tag.empty()) std::cout << tag << ": ";
    std::cout << "[";
    for (size_t i = 0; i < v.size(); ++i) {
        std::cout << v[i];
        if (i + 1 < v.size()) std::cout << ", ";
    }
    std::cout << "]\n";
}

void selectSort(std::vector<int>& a) {
    const size_t n = a.size();
    for (size_t i = 0; i < n; ++i) {
        size_t p = i;
        for (size_t j = i + 1; j < n; ++j)
            if (a[j] < a[p]) p = j;
        if (p != i) std::swap(a[i], a[p]);
    }
}

void bubbleOpt(std::vector<int>& a) {
    const size_t n = a.size();
    for (size_t pass = 0; pass < n; ++pass) {
        bool moved = false;
        for (size_t j = 1; j < n - pass; ++j) {
            if (a[j - 1] > a[j]) {
                std::swap(a[j - 1], a[j]);
                moved = true;
            }
        }
        if (!moved) break;
    }
}

static void mergeParts(std::vector<int>& a, std::vector<int>& buf, size_t L, size_t M, size_t R) {
    size_t i = L, j = M, k = L;
    while (i < M && j < R) buf[k++] = (a[i] <= a[j] ? a[i++] : a[j++]);
    while (i < M) buf[k++] = a[i++];
    while (j < R) buf[k++] = a[j++];
    for (size_t t = L; t < R; ++t) a[t] = buf[t];
}

static void mergeSortRec(std::vector<int>& a, std::vector<int>& buf, size_t L, size_t R) {
    if (R - L <= 1) return;
    size_t M = L + (R - L) / 2;
    mergeSortRec(a, buf, L, M);
    mergeSortRec(a, buf, M, R);
    mergeParts(a, buf, L, M, R);
}

void mergeSort(std::vector<int>& a) {
    std::vector<int> buf(a.size());
    mergeSortRec(a, buf, 0, a.size());
}

void shellSort(std::vector<int>& a) {
    size_t n = a.size();
    for (size_t gap = n / 2; gap > 0; gap /= 2) {
        for (size_t i = gap; i < n; ++i) {
            int x = a[i];
            size_t j = i;
            while (j >= gap && a[j - gap] > x) {
                a[j] = a[j - gap];
                j -= gap;
            }
            a[j] = x;
        }
    }
}

static void siftDown(std::vector<int>& a, size_t size, size_t i) {
    for (;;) {
        size_t largest = i, l = 2 * i + 1, r = 2 * i + 2;
        if (l < size && a[l] > a[largest]) largest = l;
        if (r < size && a[r] > a[largest]) largest = r;
        if (largest == i) break;
        std::swap(a[i], a[largest]);
        i = largest;
    }
}

void heapSort(std::vector<int>& a) {
    size_t n = a.size();
    if (n < 2) return;
    for (size_t i = n / 2; i-- > 0;) siftDown(a, n, i);
    for (size_t end = n; end-- > 1;) {
        std::swap(a[0], a[end]);
        siftDown(a, end, 0);
    }
}

int findLinear(const std::vector<int>& a, int key) {
    for (size_t i = 0; i < a.size(); ++i)
        if (a[i] == key) return static_cast<int>(i);
    return -1;
}

int findInterp(const std::vector<int>& a, int key) {
    if (a.empty()) return -1;
    size_t lo = 0, hi = a.size() - 1;
    while (lo <= hi && key >= a[lo] && key <= a[hi]) {
        if (a[lo] == a[hi]) return a[lo] == key ? static_cast<int>(lo) : -1;
        size_t pos = lo + static_cast<size_t>(
            (static_cast<long double>(key - a[lo]) * (hi - lo)) /
            static_cast<long double>(a[hi] - a[lo])
        );
        if (pos < lo || pos > hi) break;
        if (a[pos] == key) return static_cast<int>(pos);
        if (a[pos] < key) lo = pos + 1;
        else {
            if (pos == 0) break;
            hi = pos - 1;
        }
    }
    return -1;
}

int findFibo(const std::vector<int>& a, int key) {
    size_t n = a.size();
    if (n == 0) return -1;
    size_t f2 = 0, f1 = 1, f = f1 + f2;
    while (f < n) { f2 = f1; f1 = f; f = f1 + f2; }
    long long offset = -1;
    while (f > 1) {
        size_t i = std::min<size_t>(offset + f2, n - 1);
        if (a[i] < key) { f = f1; f1 = f2; f2 = f - f1; offset = static_cast<long long>(i); }
        else if (a[i] > key) { f = f2; f1 = f1 - f2; f2 = f - f1; }
        else return static_cast<int>(i);
    }
    if (f1 && offset + 1 < static_cast<long long>(n) && a[offset + 1] == key)
        return static_cast<int>(offset + 1);
    return -1;
}

int main() {
    std::vector<int> v1{64,25,12,22,11};
    std::vector<int> v2{64,34,25,12,22,11};
    std::vector<int> v3{38,27,43,3,9,82,10};
    std::vector<int> v4{23,12,1,8,34,56,7};
    std::vector<int> v5{12,11,13,5,6,7};

    auto a1 = v1; selectSort(a1); dump(a1, "select");
    auto a2 = v2; bubbleOpt(a2);  dump(a2, "bubble");
    auto a3 = v3; mergeSort(a3);  dump(a3, "merge");
    auto a4 = v4; shellSort(a4);  dump(a4, "shell");
    auto a5 = v5; heapSort(a5);   dump(a5, "heap");

    std::vector<int> s{1,3,5,7,9,11,15,20,25,30,35,40,45,50,60,70,80};
    std::cout << "linear(10): " << findLinear(std::vector<int>{3,8,1,10,5},10) << "\n";
    std::cout << "interp(35): " << findInterp(s,35) << "\n";
    std::cout << "fibo(70): "  << findFibo(s,70) << "\n";
}