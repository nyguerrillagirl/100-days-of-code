import numpy as np
costs = np.column_stack(([3, 2, 1, 3],
                         [7, 6, 6, 5]))
print(costs)
print(costs[:, 0])
mean_costs = np.mean(costs[:, 0])
print(mean_costs)