'''
Runtime comparison chart data and Scalability report
'''

def generate_runtime_comparison_chart(sizes):
    result = []

    result.append("Runtime Comparison Chart Data")
    result.append("InputSize LinearSearch BinarySearch BubbleSort InsertionSort")

    for n in sizes:
        temp = n
        binary = 0
        while temp > 0:
            temp //= 2
            binary += 1

        linear = n
        bubble = (n * (n - 1)) // 2
        insertion = bubble

        result.append(f"{n} {linear} {binary} {bubble} {insertion}")

    result.append("Scalability Summary")
    result.append("Algorithm Complexity Scalability")
    result.append("BinarySearch O(log n) Excellent")
    result.append("LinearSearch O(n) Moderate")
    result.append("BubbleSort O(n^2) Poor")
    result.append("InsertionSort O(n^2) Poor")

    result.append("Key Observations")
    result.append("Binary Search scales best with increasing input size.")
    result.append("Linear Search grows linearly with input size.")
    result.append("Bubble Sort and Insertion Sort have quadratic growth.")
    result.append("Conclusion")
    result.append("Binary Search is the most scalable algorithm, while Bubble Sort and Insertion Sort are the least scalable for large inputs.")

    return result