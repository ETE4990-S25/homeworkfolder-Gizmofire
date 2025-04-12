import math, sys



sys.set_int_max_str_digits(10000)

# exmaple 
def factorial_builtin(n):
  """Calculates the factorial of n using the built-in math.factorial() function."""
  return math.factorial(n)


def factorial_test(numT):
    num  = 0
    while True:
        if math.factorial(num) > numT:
            return math.factorial(num)
        num += 1
        print(f"The Fact number at position {num} is {math.factorial(num)}") # Output: The Fibonacci number at position 5 is 120




number = 670867

