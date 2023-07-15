from functools import wraps
import time 


def timeit(func):
    """
    a decorator function to measure function's execution time 
    """
    @wraps(func)
    def timeit_wrapper(*args , **kwargs):
        start_time = time.perf_counter()
        result = func(*args , **kwargs)
        end_time = time.perf_counter()
        total_time = end_time   - start_time 
        print(f"Function {func.__name__} took {total_time:.4f} seconds")
        return result
    return timeit_wrapper


# N + 1 = 1 + b∗ + (b∗)^2 + · · · + (b∗)^d .
def compute_effective_branching(number_of_expanded_nodes ,depth):
    """
    a newton-raphson method to compute the effective branching of search tree
    """
    MAX_ITER = 100 
    derivative = lambda b : (b**depth * ( depth*b - depth -1)) / (b -1)**2
    func = lambda b : (1-b**(depth+1))/(1 - b) - (number_of_expanded_nodes + 1)
    b = 1.5
    
    for _ in range(MAX_ITER) :
        b = b - func(b)/derivative(b)
    return b 


def generate_heuristic_report():
    pass