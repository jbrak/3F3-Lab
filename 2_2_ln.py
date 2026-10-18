# Import required libraries
from LCG import LCG
import numpy as np
import matplotlib.pyplot as plt

# Initialize the LCG with a seed value
rng = LCG(1234)

# Generate 100,000 uniform random numbers using the LCG
X = np.array([rng.uniform() for _ in range(100000)])

# Calculate Y = ln(X) - ln(1-X)
Y = np.log(X) - np.log(1 - X)

# Define the PDF of Y
y = np.linspace(-14,14, 1000)
f_Y = (np.exp(y))/((1+np.exp(y))**2)

# Plot histogram, set density to True to normalize the histogram
plt.hist(Y, bins = 30, density=True, label = "Normalized Histogram of Y")

# Plot the PDF of Y
plt.plot(y, f_Y, label = "PDF of Y", color = "red")

# Show the plot with labels and legend
plt.legend(loc = "upper left", handlelength=1, handletextpad=0.5)
plt.xlabel("y")
plt.ylabel("Frequency Density")

# Save the figure as a PDF
plt.savefig("figures/q2-log.pdf")
plt.show()


