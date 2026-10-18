from LCG import LCG
import numpy as np
import matplotlib.pyplot as plt

rng = LCG(42)

# generate uniform numbers
X1 = np.array([rng.uniform() for _ in range(1000)])
X2 = np.array([rng.uniform() for _ in range(100000)])

# Plot histograms
fig, ax = plt.subplots(2)
ax[0].hist(X1, bins=np.linspace(0,1,20))
ax[1].hist(X2, bins=np.linspace(0,1,20))
plt.show()