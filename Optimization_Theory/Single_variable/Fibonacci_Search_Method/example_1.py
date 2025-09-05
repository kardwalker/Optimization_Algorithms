from fibonacci_search_iterative import fibonacci

from math import exp, log

def example_func(x):
    return 1/(x-1)**2 * (log(x) + exp(-x))
res = fibonacci(1.5,4.5,0.01,20,example_func)
print("Extremum found between:", res)