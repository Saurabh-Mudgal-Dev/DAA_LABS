'''
Recursive and Iterative Computation Analyser
'''

def analyze_recursive_iterative(n):
    global fib_count
    fib_count=0
    return [
            "Computation Analysis Report",
            f"Recursive Factorial: {recursive_factorial(n)}",
            f"Iterative Factorial: {iterative_factorial(n)}",
            f"Recursive Fibonacci: {recursive_fibonacci(n)}",
            f"Iterative Fibonacci: {iterative_fibonacci(n)}",
            "Operation Count Comparison",
            f"Recursive Factorial Count: {n+1}",
            f"Iterative Factorial Count: {n}",
            f"Recursive Fibonacci Count: {fib_count}", 
            f"Iterative Fibonacci Count: {n}"
        ]
  
def recursive_factorial(n):
    if n in [0, 1]:
      return 1
    else:
      return (n * recursive_factorial(n-1))

def iterative_factorial(n):
  prod=1
  for i in range (1, n+1):
    prod *= i
  return prod

fib_count=0
def recursive_fibonacci(n):
  global fib_count
  fib_count+=1
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return (recursive_fibonacci(n-1) + recursive_fibonacci(n-2))
  
def iterative_fibonacci(n):
  if n == 0:
    return 0
  else:
    a,b=0,1
    for i in range(1,n):
      a,b=b,a+b
    return b