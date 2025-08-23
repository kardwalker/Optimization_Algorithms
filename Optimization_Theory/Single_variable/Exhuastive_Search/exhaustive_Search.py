

# function shoud be unimodal and continuous in given range

def exhaustive_search(func, low : int | float, high : int | float, step : int | float = 10 ,increment : float = None):
    """
    args:
        func: function to be optimized
        low: lower bound of the search space
        high: upper bound of the search space
        step: step size for the search"""
    x = low
    if low >= high:
        raise ValueError("Low must be less than high")
    assert step > 1, "Step size must be positive and greater than 1"
    detla_x = (high - low)/step
    while x <= high:
        x1 = x
        x2 = x + detla_x
        x3 = x + 2 * detla_x
        if func(x1) >= func(x2) and func(x2) <= func(x3): # minimum
            return [x1 , x3]
        elif func(x1) <= func(x2) and func(x2) >= func(x3): # maximum
            return [x1 , x3]
        x += detla_x
    return [low, high]  # If no extremum found, return the bounds
if __name__ == "__main__":
    # Example usage
    def example_func(x):
        return (x - 2) ** 2 + 1  # A simple quadratic function with a minimum at x = 2

    result = exhaustive_search(example_func, 0, 4)
    print("Extremum found between:", result)
        


    
