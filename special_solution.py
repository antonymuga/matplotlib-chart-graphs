import numpy as np

# define the coefficient matrix

A = np.array([
	[1, 2, 3, 4],
	[2, 4, 6, 8],
	[3, 6, 9, 12],
	[4, 8, 12, 16]
	])

# define the constants on the right-hand side
b = np.array([5, 10, 15, 20])

# Use NumPy's linear algebra solver to find the solution
# The special solution can be found by setting one variable to 1 and the rest to 0
special_solution = np.linalg.lstsq(A, b, rcond=None)[0]

print("Special solution:", special_solution)