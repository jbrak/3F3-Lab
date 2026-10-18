# Import required libraries
from LCG import LCG
import numpy as np
import matplotlib.pyplot as plt

# Initialize the LCG with a seed value
rng = LCG(1234)

# Generate 100,000 uniform random numbers using the LCG
X = np.array([rng.uniform() for _ in range(100000)])

# Calculate Y = X^2
Y = X**2

# Define the PDF of Y
y = np.linspace(0.01,1,1000)
f_Y = 1/(2*y**0.5)

# Plot histogram, set density to True to normalize the histogram
plt.hist(Y, bins=np.linspace(0,1,20), density=True, label = "Normalized Histogram of Y")

# Plot the PDF of Y
plt.plot(y, f_Y, label = "PDF of Y", color = "red")

# Show the plot with labels and legend
plt.legend()
plt.xlabel("y")
plt.ylabel("Frequency Density")

# Save the figure as a PDF
plt.savefig("figures/q2-square.pdf")
plt.show()


