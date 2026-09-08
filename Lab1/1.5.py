'''
Runtime and Complexity comparison table
'''

def runtime_complexity_comparison(n):
    temp = n
    binary_count = 0
    while temp > 0:
        temp //= 2
        binary_count += 1

    bubble_count = (n * (n - 1)) // 2
    insertion_count = bubble_count

    result = [
        "Runtime Complexity Comparison",
        "Method ObservedCount ExpectedComplexity Observation",
        f"LinearSearch {n} O(n) Grows linearly with input size",
        f"BinarySearch {binary_count} O(log n) Very slow growth",
        f"BubbleSort {bubble_count} O(n^2) Quadratic growth",
        f"InsertionSort {insertion_count} O(n^2) Quadratic growth"
    ]

    return result