# Import required libraries
from LCG import LCG
import numpy as np
import matplotlib.pyplot as plt

# Define a population class to handle the simulation over generations
class Population:
    def __init__(self, N, Na, seed = 1234):

        # Population Size, N
        self.N = N

        # Number of individuals with gene A, Na
        self.Na = Na

        # Number of individuals with gene B, Nb
        self.Nb = N - Na

        # Generation/Time counter
        self.t = 0

        self.rng = LCG(seed)

    def next_generation(self):
        # Calculate the probability of selecting gene A
        p_A = self.Na / self.N

        # Generate the next generation using binomial distribution
        self.Na = self.rng.binomial(self.N, p_A)

        # Update the number of individuals with gene B
        self.Nb = self.N - self.Na

        # Increment the generation counter
        self.t += 1

    def simulate(self, generations, track_history=False):
        # Simulate the population for a given number of generations

        # If the current gneration counter is greater than or equal to the specified number of generations
        # (Which defines simulation length). Return the populaton size of gene A and gene B as a dictionary
        # Otherwise generate the next generation and recursivly call the simmulate function until the above critera is met
        if self.t >= generations:
            return {"Na": self.Na, "Nb" : self.Nb} if not track_history else self.history
        else:

            # If Track history is set to true store how population sizes change over time
            # If it is the first generation, initialize the history dictionary
            # Otherwise append current population sizes to the history dictionary
            if track_history == True and self.t == 0:
                self.history = {"t" : [self.t], "Na": [self.Na], "Nb": [self.Nb]}
            elif track_history == True:
                self.history["Na"].append(self.Na)
                self.history["Nb"].append(self.Nb)
                self.history["t"].append(self.t)

            # Generate the next generation and recursively call the simulate function
            self.next_generation()
            return self.simulate(generations, track_history)


fig, ax = plt.subplots(2)

for i in range(2):
    # Initialize a population with size N= 200 and Na = 100
    population = Population(N = 200, Na = 100, seed = [1234,100][i])

    # Simulate the population for 500 generations and track the history of population sizes
    generations = 500
    history = population.simulate(generations = generations, track_history = True)

    Na = history["Na"]
    Nb = history["Nb"]
    t = history["t"]

    ax[i].plot(t,Na, label = "Na")
    ax[i].plot(t,Nb, label = "Nb")

    # Show the plot with labels and legend
    ax[i].legend(loc = "right", handlelength=1, handletextpad=0.5)
    ax[i].set_xlabel("t")
    ax[i].set_ylabel("Population Size")
    ax[i].set_title(f"Random Number Seed = {[1234,100][i]}")

# Save the figure as a PDF
plt.subplots_adjust(hspace=0.5)
plt.savefig("figures/q4-neutral-selection.pdf")
plt.show()


