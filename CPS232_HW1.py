#Aiden Atkinson - CPS232 Homework 1 - Finding the Kth Greatest Element in a List - 08/27/2026

import random
import time
import statistics

for n in [random.randint(10,20000)]:
    numbers = [random.randint(0, 1000) for _ in range(n)]
    k = n//2

print(f"The list has {n} numbers.")
print("K is:", k)
# A: find and remove the maximum k times
def kth_greatest_a(numbers, k):
    remaining = numbers.copy()
    for _ in range(k):
        kth_greatest_a = max(remaining)
        remaining.remove(kth_greatest_a)
    return kth_greatest_a


print("Maximum:", kth_greatest_a(numbers, k))

# B: sort from smallest to greatest
def kth_greatest_b(numbers, k):
    sorted_numbers = sorted(numbers)
    return sorted_numbers[len(sorted_numbers) - k]


print("Sorted Kth Greatest:", kth_greatest_b(numbers, k))


def kth_greatest_c(numbers, k):
    if len(numbers) <= 5:
        return sorted(numbers)[len(numbers) - k]

    # Make groups of five and find each group's median
    groups = [numbers[i:i + 5] for i in range(0, len(numbers), 5)]
    medians = [sorted(group)[len(group) // 2] for group in groups]

    # Find the median of those medians
    pivot = kth_greatest_c(medians, (len(medians) + 1) // 2)

    greater = [x for x in numbers if x > pivot]
    equal = [x for x in numbers if x == pivot]
    smaller = [x for x in numbers if x < pivot]

    if k <= len(greater):
        return kth_greatest_c(greater, k)

    if k <= len(greater) + len(equal):
        return pivot

    return kth_greatest_c(
        smaller,
        k - len(greater) - len(equal)
    )


kth_greatest_c_result = kth_greatest_c(numbers, k)

print("Median-of-Medians:", kth_greatest_c_result)

algorithms = {
    "A: Repeated Max": kth_greatest_a,
    "B: Sorted List": kth_greatest_b,
    "C: Median-of-Medians": kth_greatest_c
}

for name, algorithm in algorithms.items():
    times = []
    for _ in range(5):
        start = time.perf_counter()
        algorithm(numbers, k)
        times.append(time.perf_counter() - start)

    print(f"{name}: {statistics.median(times):.6f} seconds")

