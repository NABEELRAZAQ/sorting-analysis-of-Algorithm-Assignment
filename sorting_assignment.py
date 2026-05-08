import time

def selection_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if a[j] < a[min_index]:
                min_index = j
        a[i], a[min_index] = a[min_index], a[i]
    return a

def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def measure_time(sort_function, arr):

    total_time = 0

    for _ in range(3):
        start = time.time()
        sort_function(arr)
        end = time.time()
        total_time += (end - start)
    return total_time / 3
arrays = {
    "Size 5 Sorted": [1, 2, 3, 4, 5],
    "Size 5 Reverse": [5, 4, 3, 2, 1],
    "Size 100 Sorted": list(range(1, 101)),
    "Size 100 Reverse": list(range(100, 0, -1))
}
algorithms = {
    "Selection Sort": selection_sort,
    "Bubble Sort": bubble_sort,
    "Quick Sort": quick_sort,
    "Merge Sort": merge_sort
}

for algo_name, algo_function in algorithms.items():
    print("\n")
    print(algo_name)
    for case_name, arr in arrays.items():
        avg_time = measure_time(algo_function, arr)
        print(f"{case_name}: {avg_time:.10f} seconds")
