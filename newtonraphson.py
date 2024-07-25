import numdifftools as nd

def newton_raphson(func, initial_guess, tolerance=1e-10, max_iterations=100):
    x0 = initial_guess
    for _ in range(max_iterations):
        fx0 = func(x0)
        if abs(fx0) < tolerance:
            return x0
        fprime_x0 = nd.Derivative(func)(x0)
        x0 = x0 - fx0 / fprime_x0
    raise ValueError("Failed to converge")
# Example usage:
import math

def f(x):
    return x**3 - 2*x - 5
    
root = newton_raphson(f, initial_guess=3)
print(f"Root found at x = {root}")
    
