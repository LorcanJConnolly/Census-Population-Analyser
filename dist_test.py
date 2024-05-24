import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

# Test
from matplotlib.animation import FuncAnimation

df = np.load(r'C:\Users\lconn\Documents\Programming\Python\Python Projects\Population_distribution\Pop_distribution_analyser\Numpy_Arrays/UK_array.npy')
ldf = np.load(r'C:\Users\lconn\Documents\Programming\Python\Python Projects\Population_distribution\Pop_distribution_analyser\Numpy_Arrays/log_UK_array.npy')

class Population_Dist_Tester():
    def __init__(self, data):
        self.data = data
        self.desc_data = np.sort(self.data)[::-1]
        self.ln_pvalues = []
        self.p_pvalues = []

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

        res = stats.kstest(ecdf, cdf)
        ### return the pvalue
        return res.pvalue

    # FIXME: is "sample" the best term here.
    def goodness_of_fit_testing(self, sample):
        # Must be initialised with the first sample.

        # KS Tests here
        # returns the p-value from the tests which is then added to an array used for plotting
        self.ln_pvalues.append(self.KS_testing(sample, "log-normal"))
        self.p_pvalues.append(self.KS_testing(sample, "pareto"))

        # print(self.ln_pvalues)

        # Plot results as animation.
        self.plotter(sample, self.ln_pvalues, "log-normal")
        # self.plotter(sample, self.p_pvalues, "pareto")


        # Get a new sample
        sample = self.build_sample(sample)

        if len(sample) == len(self.data):
            print("Samples are equal size, STOP!")
            return len(self.ln_pvalues), len(self.p_pvalues)
            # return self.ln_pvalues
        else:
            return self.goodness_of_fit_testing(sample)

    def plotter(self, sample, p_values, distribution):
        # fig = plt.plot()
        # plt.style.use('fivethirtyeight')

        # plt.plot(sample, p_values)
        # plt.title(distribution)
        # plt.show()

        ### May need to create a new class for the animation plotting.
        pass


data = np.linspace(0, 10, num=10)
X = Population_Dist_Tester(data)
# X = Population_Dist_Tester(df)
# print(len(df)) # 10174

X.goodness_of_fit_testing(X.desc_data[:1])

# sample = X.desc_data[:10]
# p_values = np.linspace(0, 11, num=10)
# dist = "LN"
# X.plotter(sample, p_values, dist)

# print(X.KS_testing(X.desc_data[:], distribution="pareto"))
# print(X.KS_testing(X.desc_data[:], distribution="log-normal"))

# ANIMATION
# from matplotlib.animation import PillowWriter
# writer = PillowWriter(fps, metadata)

