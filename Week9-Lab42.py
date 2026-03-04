import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#uniform
uniform = np.random.uniform(-1, 1, size=5000)
print("Mean:\n", uniform.mean(), "\nStd:\n", uniform.std())

sns.histplot(uniform, bins=30, stat="density")
plt.show()

sns.kdeplot(uniform, label="N(0,1)")
plt.show()

#normal
normal = np.random.normal(loc=0, scale=1, size=5000)

print("Mean:\n", normal.mean(), "\nStd:\n", normal.std())

sns.histplot(normal, bins=40, stat="density", kde=True)
plt.show()

sns.kdeplot(normal, label="N(0,1)")
plt.show()