# import numpy as np
import numpy as np
import time

start_time = time.time()

num_points = 1000000000

# Generates random points in a square of area 4
x = np.random.uniform(-1, 1, size=num_points)
y = np.random.uniform(-1, 1, size=num_points)

# Calculates the probability of points falling in a circle of radius 1
probability_in_circle = np.sum((x ** 2 + y ** 2) < 1) / num_points

# probability_in_circle = (area of the circle) / (area of the square)

#   ==> PI = probability_in_circle * (area of the square)
print(f"PI is {probability_in_circle * 4}")

end_time = time.time()
elapsed_time = end_time - start_time
print("Elapsed time:", elapsed_time)