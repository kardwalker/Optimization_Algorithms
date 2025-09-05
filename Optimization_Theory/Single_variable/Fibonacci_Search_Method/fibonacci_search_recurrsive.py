# this code is implementation of fibonacci search method

# assumption: function is unimodal and continuous in given range

# FN+1 = FN + FN-1; for N = 1; 2; and so on
# the Fibonacci numbers are 1; 1; 2; 3; 5; 8; 13; 21; 34 ; 55; 89; 144; 233; 377; 610; 987; 1597; 2584; 4181; 6765; 10946; 17711; 28657; 46368; 75025; 121393; 196418; 317811; 514229; 832040
from re import X
from typing import Optional
def fibonacci_number(n: int) -> int:
    """Returns the n-th Fibonacci number."""
    if n <= 0:
        raise ValueError("n must be a positive integer")
    elif n == 1 or n == 2:
        return 1
    else:
        a, b = 1, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b



def fibonacci(a : int | float , b : int | float , e : float , n : int ,func, k = 2) -> int:
    """
    args:
        a: lower bound of the search space
        b: upper bound of the search space
        e: tolerance
        n: desired number of function evaluations
        k: iteration counter"""
    assert a < b, "Lower bound must be less than upper bound"
    assert e > 0, "Tolerance must be positive"
    interval_length = b - a
    l_k = fibonacci_number(n - k + 1) / fibonacci_number(n + 1) * interval_length
    X1 = a + l_k
    X2 = b - l_k
    if func(X1) < func(X2):
        b = X2
    elif func(X1) == func(X2):
         a , b = X1 , X2 
    else:
        a = X1
    if abs(b - a) < e or k == n:
        return (a, b)
    return fibonacci(a, b, e, n, func, k + 1)    
    

if __name__ == "__main__":
    # Example usage
    example_func = lambda x: (x - 2) ** 2 + 1  # A simple quadratic function with a minimum at x = 2
    result = fibonacci(0, 10, 0.01, 100, example_func)
    print("Extremum found between:", result)
    # Testing fibonacci_number function
