
from math import pow


def bounding_phase_method(func, x0 : int | float, delta : int | float = 0.001, max_iter : int = 100 ,eplison  :int | float = 1e-4 ):
    """
    args:
        func: function to be optimized
        x0: initial guess
        delta: initial step size
        max_iter: maximum number of iterations
    returns:
        a tuple (a, b) where the extremum lies in the interval [a, b]
    """
    x_minus_delta = x0 - delta
    f_minus_delta = func(x_minus_delta)
    x = x0
    f = func(x)
    x_plus_delta = x0 + delta
    f_plus_delta = func(x_plus_delta)
    k = 0
    if f_minus_delta > f > f_plus_delta :
        delta = delta # keep the same direction
    elif f_minus_delta < f < f_plus_delta :
        delta = -delta # reverse the direction
    else:
         raise ValueError("choose the different initial guess.")
    
    x1 = x + pow(2,k)*delta
    f1 = func(x1)
    while f > f1 and k < max_iter:
        k += 1
        x_minus_delta = x
        f_minus_delta = f
        f = f1
        x = x + pow(2,k)*delta
        f1 = func(x)
    print("Number of iterations:", k)
    return (x,x1) if x < x1 else (x1,x)

if __name__ == "__main__":
    # Example usage
    example_func = lambda x: (x - 2) ** 2 + 1  # A simple quadratic function with a minimum at x = 2
    result = bounding_phase_method(example_func, 0)
    print("Extremum found between:", result)