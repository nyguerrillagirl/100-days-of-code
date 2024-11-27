import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
titanic = sns.load_dataset("titanic")

# Create the bar plot
sns.barplot(data=titanic, x="class", y="survived")
plt.show()