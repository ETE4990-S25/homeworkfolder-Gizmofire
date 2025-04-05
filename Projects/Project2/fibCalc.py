import math, sys



# sys.set_int_max_str_digits(10000)


# Recursive approach
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

num  = 0
while True:
    if fibonacci_recursive(num) > 670867:
        break
    num += 1
    print(f"The Fibonacci number at position {num} is {fibonacci_recursive(num)}") # Output: The Fibonacci number at position 5 is 120



number = 670867
# result = reverse_fibonacci(number)
print(f"The factorial of {number} is ") # Output: The factorial of 5 is 120


