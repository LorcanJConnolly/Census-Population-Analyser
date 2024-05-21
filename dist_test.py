import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

df = np.load(r'C:\Users\lconn\Documents\Programming\Python\Python Projects\Population_distribution\Pop_distribution_analyser\Numpy_Arrays/UK_array.npy')
ldf = np.load(r'C:\Users\lconn\Documents\Programming\Python\Python Projects\Population_distribution\Pop_distribution_analyser\Numpy_Arrays/log_UK_array.npy')

# Get data
# Order from largest to smallest (descending)
# build up an sample array by popping from the data largest to smallest
# test the sample array
    # Get the Pareto and Log-normal fit parameters
    # KS test the two distributions
# Plot the ks test results
# Plot an animation of the distributions and their parameters as the sample array builds up


# Three functions: One that builds the sample,  one that does the KS tests, one that plots.
class Population_Dist_Tester():
    def __init__(self, data):
        self.data = data
        self.desc_data = np.sort(self.data)[::-1]

    def build_sample(self, sample):
        # Takes the sample, reassigns the sample pointer to a one bigger slice of the data set.
        return self.desc_data[:len(sample)+1]
    
    def KS_testing(self, data):
        # Must be initialised with the first sample.

        # Get the sample from build_sample
        # Fit the parameters for the Pareto empirical cdf and Log-normal empirical cdf
        # preform the KS testing on the two cdfs
        # returns the values from the tests

        # KS Tests here

        # Get a new sample
        sample = self.build_sample(sample)
        print(f"sample is: {sample}")
        if len(sample) == len(self.data):
            print("Samples are equal size, STOP!")
            return "KS Values here"
        else:
            self.KS_testing(data=sample)


data = np.linspace(0, 10, num=20)
X = Population_Dist_Tester(data)

print(X.KS_testing(X.desc_data[:11]))

# ANIMATION
# from matplotlib.animation import PillowWriter
# writer = PillowWriter(fps, metadata)

