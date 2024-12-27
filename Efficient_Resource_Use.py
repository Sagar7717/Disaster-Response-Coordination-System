# resource_optimization.py
import numpy as np
from scipy.optimize import linprog

# Define resource requirements and availability
# Example data: [water, food, medical kits, blankets]
requirements = np.array([
    [3, 2, 1, 4],  # Location A
    [5, 3, 2, 1],  # Location B
    [2, 4, 3, 2],  # Location C
])

available_resources = np.array([100, 80, 50, 60])

# Cost of sending resources (arbitrary values for demonstration)
costs = np.array([
    [1, 2, 3],  # Water
    [2, 1, 3],  # Food
    [3, 3, 1],  # Medical kits
    [4, 2, 1],  # Blankets
]).T.flatten()

# Flatten the requirements for linear programming
req_flatten = requirements.flatten()

# Bounds for resources (non-negative allocations)
bounds = [(0, available_resources[i // 3]) for i in range(len(req_flatten))]

# Constraints to ensure each location's demand is met
A_eq = []
for i in range(requirements.shape[0]):
    row = np.zeros_like(req_flatten)
    row[i * requirements.shape[1]:(i + 1) * requirements.shape[1]] = 1
    A_eq.append(row)

b_eq = [1] * requirements.shape[0]  # Demand fulfillment constraint

# Solve the optimization problem
result = linprog(costs, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')

if result.success:
    allocations = result.x.reshape(requirements.shape)
    print("Optimized Resource Allocation:")
    print(allocations)
else:
    print("Optimization failed.")
