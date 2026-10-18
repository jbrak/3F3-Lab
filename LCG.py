
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
        # to be completed
        pass

if __name__ == "__main__":
    # Example usage of the LCG class
    rng = LCG(42)

    # Generate and print random numbers using the LCG
    print(rng())
    print(rng())
    print(rng.uniform())
    print(rng.uniform())
