import random
import time
from heapsort import heapsort
from insertionsort import insertion_sort
from mergesort import merge_sort
from quicksort import quick_sort
from selectionsort import selection_sort
import sys

sys.setrecursionlimit(100000)

def gen_extreme_list(size, small_range=(0, 100), outlier_range=(10000, 20000), outlier_ratio=0.01):
    num_outliers = int(size * outlier_ratio)
    num_small_values = size - num_outliers
    small_values = [random.randint(*small_range) for _ in range(num_small_values)]
    outlier_values = [random.randint(*outlier_range) for _ in range(num_outliers)]
    combined = small_values + outlier_values
    random.shuffle(combined)
    return combined

def quick_sort_wrapper(arr):
    return quick_sort(arr, 0, len(arr) - 1)  # Wrap quick_sort with the correct arguments

def test_and_time(algorithm_name, sort_fn, description, data):
    arr = data.copy()
    start = time.time()
    result = sort_fn(arr)
    end = time.time()

    # If function returns a new sorted list
    if result is not None:
        arr = result

    # Ensure the array is sorted correctly
    assert arr == sorted(data), f"{algorithm_name} failed to sort properly!"
    
    # Formatting output for clarity
    print(f"\033[1m{algorithm_name}\033[0m on \033[4m{description}\033[0m: "
          f"\033[92m{end - start:.4f} sec\033[0m")  # Green color for time

def test_performance():
    sizes = [1000, 5000, 10000, 20000, 30000, 40000, 50000, 100000, 500000]  # Sizes for testing
    algorithms = [
        ("HeapSort", heapsort),
        ("InsertionSort", insertion_sort),
        ("MergeSort", merge_sort),
        ("QuickSort", quick_sort),  # Use the wrapper for quick_sort
        ("SelectionSort", selection_sort)
    ]
    
    # Header for the overall test
    print("\033[1m\033[4mPerformance Testing: Sorting Algorithms\033[0m\n")
    
    for size in sizes:
        print(f"\n\033[1m=== Testing with size: {size} ===\033[0m")
        test_cases = [
            ("Random List", [random.randint(0, 1000) for _ in range(size)]),
            ("Reverse Sorted List", list(range(size))[::-1]),
            ("Extreme Value List", gen_extreme_list(size)),
            ("Many Duplicates", [random.choice([5, 10, 20, 50]) for _ in range(size)])
        ]

        for description, data in test_cases:
            print(f"\n\033[1mTesting case: {description} ({size})\033[0m")
            print("-" * 50)  # Separator line
            for algo_name, algo_fn in algorithms:
                test_and_time(algo_name, algo_fn, description, data)
            print("-" * 50)  # Separator line for each test case

if __name__ == "__main__":
    test_performance()
