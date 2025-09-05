from math import exp , cos
from fibonacci_search_iterative import fibonacci

def example_func(x):
    return exp(-x) - cos(x)  # A function with a minimum

res = fibonacci(0,10,0.01,100,example_func)
print("Extremum found between:", res)