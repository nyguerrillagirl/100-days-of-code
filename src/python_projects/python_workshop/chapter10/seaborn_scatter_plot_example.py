import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset("tips")

# Create the scatter plot
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex")
plt.show()