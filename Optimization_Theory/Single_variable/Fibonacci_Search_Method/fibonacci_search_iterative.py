# this code is implementation of fibonacci search method

# assumption: function is unimodal and continuous in given range

# FN+1 = FN + FN-1; for N = 1; 2; and so on
# the Fibonacci numbers are 1; 1; 2; 3; 5; 8; 13; 21; 34 ; 55; 89; 144; 233; 377; 610; 987; 1597; 2584; 4181; 6765; 10946; 17711; 28657; 46368; 75025; 121393; 196418; 317811; 514229; 832040


def fibonacci(a: float, b: float, e: float, n: int, func, k: int = 1) -> tuple[float, float]:
    """Iterative Fibonacci search that avoids recursion.

    Args:
        a: lower bound
        b: upper bound
        e: tolerance (stop when interval length < e)
        n: number of Fibonacci steps (should be >= 2)
        func: objective function (unimodal)

    Returns:
        A tuple (a, b) representing the final interval containing the minimum.
    """
    assert a < b, "Lower bound must be less than upper bound"
    assert e > 0, "Tolerance must be positive"
    if n < 2:
        raise ValueError("n must be >= 2")

    # Precompute fibonacci numbers up to n+1 (1-based sequence: F1=1, F2=1)
    fib = [0, 1, 1]
    for i in range(3, n + 2):
        fib.append(fib[-1] + fib[-2])

    interval_length = b - a

    # Iterative loop: k goes from 1 to n-1 (at most n-1 function comparisons)
    for k in range(1, n):
        if abs(b - a) < e:
            break

        # length proportion for this iteration
        l_k = fib[n - k + 1] / fib[n + 1] * (b - a)
        x1 = a + l_k
        x2 = b - l_k

        f1 = func(x1)
        f2 = func(x2)

        if f1 < f2:
            # minimum in [a, x2]
            b = x2
        elif f1 > f2:
            # minimum in [x1, b]
            a = x1
        else:
            # equal, shrink to [x1, x2]
            a, b = x1, x2

    return (min(a, b), max(a, b))
    

if __name__ == "__main__":
    # Example usage
    example_func = lambda x: (x - 2) ** 2 + 1  # A simple quadratic function with a minimum at x = 2
    result = fibonacci(0, 4, 0.01, 100, example_func)
    print("Extremum found between:", result)
    # Testing fibonacci_number function
