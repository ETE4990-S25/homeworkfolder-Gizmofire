# Project # 2


Links to an external site.
Create a Multiprocessing, Threaded and Asynchronous application that will 
 - calculate the highest prime number in 3 min.
 - Calculates the Fibonacci number of that prime.
    - ie if the highest prime is 13,386,001 then calculate Fibonacci to that number
- Calculates the factorial that a given number.
once the prime is calculated you may perform Fibonacci and Factorial at the same time. 

For primes you must start a 0

 

For code constancy use the following is_prime function.
```
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
```


```
These are my results:
Multi core:71,161,003 (7)
Asycn: 960,737 (1)
Threaded 10,747,921 (10)
```