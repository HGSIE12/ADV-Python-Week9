import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Define distribution
dist = stats.norm(0, 1)

# Range
a, b = -1, 1

# P(a <= X <= b) using CDF
prob = dist.cdf(b) - dist.cdf(a)
print("P(a ≤ X ≤ b):", prob)

# Quantile using PDF
print("95th percentile:", dist.pdf(0.95))

# Plot CDF
x = np.linspace(-4, 4, 100)
plt.plot(x, dist.cdf(x))
plt.axvline(a, linestyle="--")
plt.axvline(b, linestyle="--")
plt.title("Normal CDF")
plt.show()