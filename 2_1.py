# Import required libraries
from LCG import LCG
import numpy as np
import matplotlib.pyplot as plt

# Initialize the LCG with a seed value
rng = LCG(1234)

print("Random numbers generated using LCG:")
for i in range(5):
    print(rng.uniform())

# generate uniform numbers
X1 = np.array([rng.uniform() for _ in range(1000)])
X2 = np.array([rng.uniform() for _ in range(100000)])

# Plot histograms
fig, ax = plt.subplots(2)
ax[0].hist(X1, bins=np.linspace(0,1,20))
ax[0].set_title("X1, 1,000 samples")
ax[1].hist(X2, bins=np.linspace(0,1,20))
ax[1].set_title("X2, 100,000 samples")

# Add labels to the axes
ax[0].set_xlabel("x")
ax[0].set_ylabel("Count")
ax[1].set_xlabel("x")
ax[1].set_ylabel("Count")

# Adjust the spacing between subplots
plt.subplots_adjust(hspace=0.5)
plt.show()

# Save the figure as a PDF
fig.savefig("figures/q1-histograms.pdf")

# Calculate mean and variance
mean_X2 = np.mean(X2)
var_X2 = np.var(X2)

print("X1 = 1000 uniform random numbers")
print("X2 = 100000 uniform random numbers")

print(f"Mean of X2: {mean_X2}, Variance of X2: {var_X2}")

# Create X2t and X2tp1 arrays for covariance calculation
X2tp1 = np.copy(X2)
X2t = np.copy(X2)

X2tp1 = X2tp1[1:]
X2t = X2t[:-1]

# Calculate covariance between X2t and X2tp1
# Take the [0,1] (or [1,0]) element of the matrix as this corresponds to the covariance between X2t and X2tp1
# Diagonals elements are the variances of X2t and X2tp1, respectively
covarience = np.cov(X2t, X2tp1)[0,1]

print("X2t = Xt values of X2 from index 0 to 99998")
print("X2tp1 = Xt+1 values of X2 from index 1 to 99999")

print(f"Covarience of X2t and X2tp1: {covarience}")