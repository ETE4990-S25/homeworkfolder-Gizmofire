import math, sys



sys.set_int_max_str_digits(10000)


def factorial_builtin(n):
  """Calculates the factorial of n using the built-in math.factorial() function."""
  return math.factorial(n)

num  = 0
while True:
    if factorial_builtin(num) > 670867:
        break
    num += 1
    print(f"The Fibonacci number at position {num} is {factorial_builtin(num)}") # Output: The Fibonacci number at position 5 is 120




number = 670867

