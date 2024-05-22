import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

df = np.load(r'C:\Users\lconn\Documents\Programming\Python\Python Projects\Population_distribution\Pop_distribution_analyser\Numpy_Arrays/UK_array.npy')
ldf = np.load(r'C:\Users\lconn\Documents\Programming\Python\Python Projects\Population_distribution\Pop_distribution_analyser\Numpy_Arrays/log_UK_array.npy')

class Population_Dist_Tester():
    def __init__(self, data):
        self.data = data
        self.desc_data = np.sort(self.data)[::-1]

    def build_sample(self, sample):
        # Takes the sample, reassigns the sample pointer to a one bigger slice of the data set.
        return self.desc_data[:len(sample)+1]
    
    def KS_testing(self, data, distribution):
        # FIXME: documentation
        # Fit the parameters for the Pareto empirical cdf and Log-normal empirical cdf
        # preform the KS testing on the two cdfs
        # returns the values from the tests
        
        # scipy.stats.kstest(rvs, cdf)
        # (rvs parameter) EMPIRICAL CDF values (assuming Pareto/Log-normal) are just the values in our sample as a STEP FUNCTION since it is in descending order.
        # (cdf parameter) We have to create what the ACTUAL cdf values of the Pareto/Log-normal cdf distribution would be if it had the parameters derived from our sample.

        if distribution == "log-normal":
            shape, loc, scale = stats.lognorm.fit(data)
            # print(shape, loc, scale)
            cdf = stats.lognorm.cdf(data, shape, loc, scale)
        if distribution == "pareto":
            b, loc, scale = stats.pareto.fit(data)
            # print(b, loc, scale)
            cdf = stats.pareto.cdf(data, b, loc, scale)
            
        ecdf = np.arange(len(data), 0, -1) / len(data)   # empircial cdf is just a step function.

        # == PLOTS FOR TESTING ==
        # test_fig = plt.figure()
        # plt.plot(data, cdf)
        # plt.plot(data, ecdf)
        # plt.show()

        # You can either compare the statistic value given by python to the KS-test critical value table according to your sample size.
        # When statistic value is higher than the critical value, the two distributions are different.

        # Or you can compare the p-value to a level of significance a, usually a=0.05 or 0.01 (you decide, the lower a is, the more significant). 
        ### If p-value is lower than a, then it is very probable that the two distributions are different.

        print(stats.kstest(ecdf, cdf)) 

        # return the p-value
        return "DONE"

    # FIXME: is "sample" the best term here.
    def goodness_of_fit_testing(self, sample):
        # Must be initialised with the first sample.

        # KS Tests here
        # returns the p-value from the tests which is then added to an array used for plotting
        ks_ln_res = self.KS_testing(sample, "log-normal")
        ks_p_res = self.KS_testing(sample, "pareto")

        # Plot results as animation.
        
        # Get a new sample
        sample = self.build_sample(sample)

        if len(sample) == len(self.data):
            print("Samples are equal size, STOP!")
            return "KS Values here"
        else:
            self.KS_testing(sample)


data = np.linspace(0, 10, num=20)
# X = Population_Dist_Tester(data)
X = Population_Dist_Tester(df)

# print(X.goodness_of_fit_testing(X.desc_data[:11]))
print(X.KS_testing(X.desc_data[:], distribution="pareto"))
print(X.KS_testing(X.desc_data[:], distribution="log-normal"))

# ANIMATION
# from matplotlib.animation import PillowWriter
# writer = PillowWriter(fps, metadata)

