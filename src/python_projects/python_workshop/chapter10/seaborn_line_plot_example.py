import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
fmri = sns.load_dataset("fmri")

# Create the line plot
sns.lineplot(data=fmri, x="timepoint", y="signal", hue="event")
plt.show()