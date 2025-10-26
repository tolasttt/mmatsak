def select_min_sort(seq):
    length = len(seq)
    for left in range(length - 1):
        pos_min = left
        for k in range(left + 1, length):
            if seq[k] < seq[pos_min]:
                pos_min = k
        seq[left], seq[pos_min] = seq[pos_min], seq[left]


def demo_select_min_sort():
    data = [64, 25, 12, 22, 11]
    print("Стартовый список:")
    show(data)
    select_min_sort(data)
    print("\nПосле сортировки выбором:")
    show(data)


def bubble_sort_fast(items):
    n = len(items)
    for pass_idx in range(n - 1):
        swapped = False
        for i in range(0, n - pass_idx - 1):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
                swapped = True
        if not swapped:
            break


def demo_bubble_sort_fast():
    arr = [64, 34, 25, 12, 22, 11]
    print("Стартовый список:")
    show(arr)
    bubble_sort_fast(arr)
    print("\nПосле сортировки пузырьком:")
    show(arr)


def insert_sort(nums):
    for idx in range(1, len(nums)):
        cur = nums[idx]
        j = idx - 1
        while j >= 0 and nums[j] > cur:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = cur


def demo_insert_sort():
    sample = [12, 11, 13, 5, 6]
    print("Стартовый список:")
    show(sample)
    insert_sort(sample)
    print("\nПосле сортировки вставками:")
    show(sample)


def merge_sort_new(values):
    if len(values) <= 1:
        return values
    mid = len(values) // 2
    left = merge_sort_new(values[:mid])
    right = merge_sort_new(values[mid:])
    return _merge_parts(left, right)


def _merge_parts(a, b):
    merged = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i]); i += 1
        else:
            merged.append(b[j]); j += 1
    if i < len(a):
        merged.extend(a[i:])
    if j < len(b):
        merged.extend(b[j:])
    return merged


def demo_merge_sort_new():
    src = [38, 27, 43, 3, 9, 82, 10]
    print("Стартовый список:")
    show(src)
    sorted_copy = merge_sort_new(src)
    print("\nПосле сортировки слиянием:")
    show(sorted_copy)


def shell_sort_simple(seq):
    gap = len(seq) // 2
    while gap > 0:
        for i in range(gap, len(seq)):
            temp = seq[i]
            j = i
            while j >= gap and seq[j - gap] > temp:
                seq[j] = seq[j - gap]
                j -= gap
            seq[j] = temp
        gap //= 2


def demo_shell_sort_simple():
    nums = [23, 12, 1, 8, 34, 56, 7]
    print("Стартовый список:")
    show(nums)
    shell_sort_simple(nums)
    print("\nПосле сортировки Шелла:")
    show(nums)


def quicksort_inplace(a, lo=0, hi=None):
    if hi is None:
        hi = len(a) - 1
    if lo < hi:
        p = _partition_lomuto(a, lo, hi)
        quicksort_inplace(a, lo, p - 1)
        quicksort_inplace(a, p + 1, hi)


def _partition_lomuto(a, lo, hi):
    pivot = a[hi]
    i = lo - 1
    for j in range(lo, hi):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[hi] = a[hi], a[i + 1]
    return i + 1


def demo_quicksort_inplace():
    data = [10, 7, 8, 9, 1, 5]
    print("Стартовый список:")
    show(data)
    quicksort_inplace(data)
    print("\nПосле быстрой сортировки:")
    show(data)


def heapsort(values):
    n = len(values)
    for i in range(n // 2 - 1, -1, -1):
        _sift_down(values, n, i)
    for end in range(n - 1, 0, -1):
        values[0], values[end] = values[end], values[0]
        _sift_down(values, end, 0)


def _sift_down(h, size, root):
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2
    if left < size and h[left] > h[largest]:
        largest = left
    if right < size and h[right] > h[largest]:
        largest = right
    if largest != root:
        h[root], h[largest] = h[largest], h[root]
        _sift_down(h, size, largest)


def demo_heapsort():
    nums = [12, 11, 13, 5, 6, 7]
    print("Стартовый список:")
    show(nums)
    heapsort(nums)
    print("\nПосле пирамидальной сортировки:")
    show(nums)


def find_linear(seq, target):
    for idx, val in enumerate(seq):
        if val == target:
            return idx
    return -1


def demo_find_linear():
    seq = [3, 8, 1, 10, 5]
    needle = 10
    pos = find_linear(seq, needle)
    if pos != -1:
        print(f"Элемент {needle} найден на позиции {pos}")
    else:
        print(f"Элемент {needle} отсутствует")


def find_binary(sorted_seq, target):
    lo, hi = 0, len(sorted_seq) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2
        if sorted_seq[mid] == target:
            return mid
        if sorted_seq[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1


def demo_find_binary():
    ordered = [1, 3, 5, 7, 9, 11]
    key = 7
    pos = find_binary(ordered, key)
    if pos != -1:
        print(f"Значение {key} находится по индексу {pos}")
    else:
        print(f"Значение {key} не найдено")


def search_interpolation(arr, key):
    low, high = 0, len(arr) - 1
    while low <= high and arr[low] <= key <= arr[high]:
        if low == high:
            return low if arr[low] == key else -1
        span = arr[high] - arr[low]
        if span == 0:
            pos = low
        else:
            pos = low + (key - arr[low]) * (high - low) // span
        pos = max(low, min(pos, high))
        if arr[pos] == key:
            return pos
        if arr[pos] < key:
            low = pos + 1
        else:
            high = pos - 1
    return -1


def demo_search_interpolation():
    ordered = [10, 15, 20, 25, 30, 35, 40, 45, 50]
    key = 35
    pos = search_interpolation(ordered, key)
    if pos != -1:
        print(f"Значение {key} найдено по индексу {pos}")
    else:
        print(f"Значение {key} не найдено в массиве")


def search_fibonacci(arr, key):
    n = len(arr)
    fm2, fm1 = 0, 1
    fm = fm2 + fm1
    while fm < n:
        fm2, fm1 = fm1, fm
        fm = fm2 + fm1
    offset = -1
    while fm > 1:
        i = min(offset + fm2, n - 1)
        if arr[i] < key:
            fm = fm1
            fm1 = fm2
            fm2 = fm - fm1
            offset = i
        elif arr[i] > key:
            fm = fm2
            fm1 = fm1 - fm2
            fm2 = fm - fm1
        else:
            return i
    if fm1 and offset + 1 < n and arr[offset + 1] == key:
        return offset + 1
    return -1


def demo_search_fibonacci():
    ordered = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
    key = 85
    pos = search_fibonacci(ordered, key)
    if pos != -1:
        print(f"Элемент {key} найден по индексу {pos}")
    else:
        print(f"Элемент {key} не обнаружен")


def show(seq):
    print(" ".join(map(str, seq)))


if __name__ == "__main__":
    print("=== ВЫБОР — SELECT MIN SORT ===")
    demo_select_min_sort()

    print("\n=== ПУЗЫРЁК — BUBBLE SORT ===")
    demo_bubble_sort_fast()

    print("\n=== ВСТАВКИ — INSERTION SORT ===")
    demo_insert_sort()

    print("\n=== СЛИЯНИЕ — MERGE SORT ===")
    demo_merge_sort_new()

    print("\n=== ШЕЛЛ — SHELL SORT ===")
    demo_shell_sort_simple()

    print("\n=== БЫСТРАЯ — QUICKSORT ===")
    demo_quicksort_inplace()

    print("\n=== ПИРАМИДА — HEAP SORT ===")
    demo_heapsort()

    print("\n=== ПОИСК — ЛИНЕЙНЫЙ ===")
    demo_find_linear()

    print("\n=== ПОИСК — БИНАРНЫЙ ===")
    demo_find_binary()

    print("\n=== ПОИСК — ИНТЕРПОЛЯЦИОННЫЙ ===")
    demo_search_interpolation()

    print("\n=== ПОИСК — ФИБОНАЧЧИ ===")
    demo_search_fibonacci()
