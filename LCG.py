
# Linear Congruential Generator (LCG) implementation in Python
class LCG(object):
    def __init__(self, seed):
        # Initialize the LCG with a seed value
        self.__X = int(seed)

    def __call__(self):
        # Update the internal state using the LCG formula
        self.__X = (1664525 * self.__X + 1013904223) % 4294967296
        return self.__X

    def uniform(self):
        # Return a uniform random number in the range [0, 1)
        return self() / 4294967296

    def bernoulli(self, p):
        # Return a Bernoulli random variable with probability p

        # If the uniform random number is less than or equal to p, return 1 otherwise return 0
        # This is because the probability of getting a 1 is p,
        # and thus the fraction of decimals between 0 and 1 that are less than or equal to p = p
        # Thus resulting in a Bernoulli random variable with probability p
        return 1 if self.uniform() <= p else 0

    def binomial(self, n, p):
        # Return a Binomial random variable with parameters n and p

        # Initialize a variable to keep track of the total number of successes
        total = 0

        # Binomial is the sum of n independent Bernoulli random variables with probability p
        for i in range(n):
            total += self.bernoulli(p)

        # Return the total number of successes in n trials
        return total

if __name__ == "__main__":
    # Example usage of the LCG class
    rng = LCG(42)

    # Generate and print random numbers using the LCG
    print(rng())
    print(rng())
    print(rng.uniform())
    print(rng.uniform())
