from exhaustive_Search import exhaustive_search

def function_to_optimize(x):
    return (x) ** 2 + 54/x  # A function with a minimum at x = 3

res = exhaustive_search(function_to_optimize, 1, 5, step= 10)
print("Extremum found between:", res)