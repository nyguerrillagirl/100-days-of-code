import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(100)
y = np.random.rand(100)

plt.scatter(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot')
plt.show()