
from bounding_phase_method import bounding_phase_method

# example
def func(x):
    return (x) ** 2 + 54/x  # A function with a minimum at x = 3

result = bounding_phase_method(func, x0=1, delta=0.001, max_iter=100)
print("Extremum found between:", result)