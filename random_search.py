import numpy as np
from lecture import complex_math

def random_search(function, num_samples=1000, bounds=(-100, 100)):
    best_x, best_y = None, None
    best_output = float('inf')

    for _ in range(num_samples):
        # Generate random x, y within the bounds
        # TODO: Can we make this random sampling more efficient?
        x = np.random.randint(*bounds)
        y = np.random.randint(*bounds)
        value = function(x, y)

        if value < best_output:
            best_x, best_y, best_output = x, y, value

    return best_x, best_y, best_output


if __name__ == '__main__':
    x, y, v = random_search(function=complex_math)  # Find the best (x, y) that minimises the value of function(x, y)
    print(f"Best x: {x}")
    print(f"Best y: {y}")
    print(f"Best output: {v}")