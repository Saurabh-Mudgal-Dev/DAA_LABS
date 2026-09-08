'''
Algorithm execution Observation table
'''

def generate_execution_observation_table(sizes):
    memo = {0: 1, 1: 1}

    def get_fib_calls(n):
        if n not in memo:
            memo[n] = get_fib_calls(n - 1) + get_fib_calls(n - 2) + 1
        return memo[n]

    def binary_search_steps(n):
        count = 0
        while n > 0:
            n //= 2
            count += 1
        return count

    result = [
        "Algorithm Execution Observation Table",
        "InputSize RecursiveFactorial IterativeFactorial RecursiveFibonacci IterativeFibonacci LinearSearch BinarySearch BubbleSort InsertionSort"
    ]

    for n in sizes:
        rec_fact = n + 1
        iter_fact = n
        rec_fib = get_fib_calls(n)
        iter_fib = n
        lin_search = n
        bin_search = binary_search_steps(n)

        bub_sort = (n * (n - 1)) // 2
        ins_sort = (n * (n - 1)) // 2

        row = f"{n} {rec_fact} {iter_fact} {rec_fib} {iter_fib} {lin_search} {bin_search} {bub_sort} {ins_sort}"
        result.append(row)

    return result