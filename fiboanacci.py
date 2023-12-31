def fibonacci(n):
    fib_series = [0, 1]

    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])

    return fib_series

num_terms = int(input("Enter the number of terms for the Fibonacci series: "))
result = fibonacci(num_terms)
print("Fibonacci Series:")
print(result)   