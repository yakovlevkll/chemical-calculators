import numpy as np

reaction = 'CO2 + H2O = C6H12O6 + O2'
solution = [6, 6, 1, 6]

coeffs = np.array([[1, 0, -6, 0],
                   [2, 1, -6, -2],
                   [0, 2, -12, 0]])

reaction = 'Al + HNO3 = Al(NO3)3 + NH4NO3 + H2O'
solution = [8, 30, 8, 3, 9]

coeffs = np.array([[1, 0, -1, 0, 0],
                   [0, 1, 0, -4, -2],
                   [0, 1, -3, -2, 0],
                   [0, 3, -9, -3, -1]])

# The system of linear equations to be solved is represented in the form of matrix AX = B

# Select all columns except the last one
A = coeffs[:, :-1]

# Select the last column
B = -coeffs[:, -1]

# Solution could be found as X = A^-1 * B
X = np.linalg.inv(A).dot(B)

# Alternative way
# X = np.linalg.solve(A, B)

for i in range(1, 10):
    probe = i * X
    probe_int = np.around(probe, decimals=2)

    if np.allclose(probe, probe_int):
        solution = list(probe_int.astype(int))
        solution.append(i)
        print(solution)
        break
