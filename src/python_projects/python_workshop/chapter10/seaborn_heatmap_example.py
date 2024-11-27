import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
flights = sns.load_dataset("flights")
flights = flights.pivot(index="month", columns="year", values="passengers")

# Create the heatmap
sns.heatmap(flights, cmap="YlGnBu")
plt.show()
