import time
import random
import matplotlib.pyplot as plt


def insertion_sort(a):
    a = a[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result + left[i:] + right[j:]


def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a) // 2]
    less = [x for x in a if x < pivot]
    equal = [x for x in a if x == pivot]
    greater = [x for x in a if x > pivot]
    return quick_sort(less) + equal + quick_sort(greater)


def python_sorted(a):
    return sorted(a)


algorithms = {
    "Insertion": insertion_sort,
    "Merge": merge_sort,
    "Quick": quick_sort,
    "Python sorted": python_sorted,
}

sizes = [10**3, 10**4, 10**5]
kinds = ["Sorted", "Reversed", "Random"]


def make_data(kind, n):
    data = list(range(n))
    if kind == "Sorted":
        return data
    if kind == "Reversed":
        return data[::-1]
    random.shuffle(data)
    return data


def measure(func, data):
    start = time.perf_counter()
    func(data)
    return time.perf_counter() - start


plt.figure(figsize=(15, 4))

for k, kind in enumerate(kinds, 1):
    plt.subplot(1, 3, k)
    for name, func in algorithms.items():
        times = []
        for n in sizes:
            if name == "Insertion" and n > 10**4:
                times.append(float("nan"))
            else:
                times.append(measure(func, make_data(kind, n)))
        plt.plot(sizes, times, marker="o", label=name)
    plt.xscale("log")
    plt.yscale("log")
    plt.title(kind)
    plt.xlabel("n")
    plt.ylabel("Time (s)")
    plt.legend()

plt.tight_layout()
plt.show()
