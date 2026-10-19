# Import required libraries
from LCG import LCG
import numpy as np
import matplotlib.pyplot as plt

# Initialize the LCG with a seed value
rng = LCG(1234)

# Generate 100,000 uniform random numbers using the LCG
X = np.array([rng.uniform() for _ in range(100000)])

# Using the inverse CDF method to generate random numbers form the distribution of Y ~ Exp(1)
Y_sample = - np.log(1-X)

# Define the PDF of Y
y = np.linspace(-0, 12, 1000)
Y_pdf = np.exp(-y)

# Plot histogram, set density to True to normalize the histogram
plt.hist(Y_sample, bins = 30, density=True, label = "Y Sampled using the Inverse CDF Method")

# Plot the PDF of Y
plt.plot(y, Y_pdf, label = "PDF of Y", color = "red")

# Show the plot with labels and legend
plt.legend(loc = "upper left", handlelength=1, handletextpad=0.5)
plt.xlabel("y")
plt.ylabel("Frequency Density")

# Save the figure as a PDF
plt.savefig("figures/q3-exponential.pdf")
plt.show()


