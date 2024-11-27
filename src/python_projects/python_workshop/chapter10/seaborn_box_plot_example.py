import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset("tips")

# Create the box plot
sns.boxplot(data=tips, x="day", y="total_bill")
plt.show()