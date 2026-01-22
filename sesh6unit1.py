# Trigonometric Function Table
In this notebook, we define functions to calculate `sin(x)` and `cos(x)`, tabulate their values for `x` between 0 and 2, and display the first 10 values in a formatted table.
import numpy as np

def my_sin(x):
    """
    Returns the sine of x.
    
    Parameters:
    x (float or array-like): Input value(s) in radians.
    
    Returns:
    float or array-like: sin(x)
    """
    return np.sin(x)
## cos(x) Function
This function calculates the cosine of a given input `x`.
def my_cos(x):
    """
    Returns the cosine of x.
    
    Parameters:
    x (float or array-like): Input value(s) in radians.
    
    Returns:
    float or array-like: cos(x)
    """
    return np.cos(x)
## Tabulate sin(x) and cos(x)
We will now create arrays of `x` between 0 and 2 with 1000 points, and use our functions to compute `sin(x)` and `cos(x)` for each value.
# Number of points
num_points = 1000

# Tabulate x values between 0 and 2
x_values = np.linspace(0, 2, num_points)

# Compute sin(x) and cos(x) using the defined functions
sin_values = my_sin(x_values)
cos_values = my_cos(x_values)
## Print First 10 Values
We will use a for loop to print the first 10 values of `x`, `sin(x)`, and `cos(x)` in columns.
# Print header
print(f"{'x':>8} {'sin(x)':>12} {'cos(x)':>12}")

# Loop through the first 10 entries
for i in range(10):
    print(f"{x_values[i]:8.4f} {sin_values[i]:12.6f} {cos_values[i]:12.6f}")
