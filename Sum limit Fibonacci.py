def fibonacci_sum_even(limit):
    fib_prev = 1
    fib_current = 2

    even_sum = 0

    while fib_current <= limit:
        if fib_current % 2 == 0:
            even_sum += fib_current
        fib_prev, fib_current = fib_current, fib_prev + fib_current

    return even_sum


limit = 100

result_sum = fibonacci_sum_even(limit)
print(f"The sum of even-valued terms in the Fibonacci series up to {limit} is: {result_sum}")
