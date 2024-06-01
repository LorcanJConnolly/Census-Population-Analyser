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
        self.ln_pvalues = []
        self.p_pvalues = []
    
    def KS_testing(self, data, distribution):
        ### Preforms a two sample KS test between the sample's empircial cdf step funciton and the Pareto/Log-normal cdf calcualted from fitting parameters to the sample. ###
        ### Retuns the calcualted p-value from the KS test. ###
        if distribution == "log-normal":
            shape, loc, scale = stats.lognorm.fit(data)
            cdf = stats.lognorm.cdf(data, shape, loc, scale)
        if distribution == "pareto":
            b, loc, scale = stats.pareto.fit(data)
            cdf = stats.pareto.cdf(data, b, loc, scale)
        ecdf = np.arange(len(data), 0, -1) / len(data)   # empircial cdf is just a step function.
        res = stats.kstest(ecdf, cdf)
        return res.pvalue

    def goodness_of_fit_testing(self):
        ###
        #FIXME: maybe change step length to 10.
        for n in range(1, len(self.data)+1):
            self.ln_pvalues.append(self.KS_testing(self.desc_data[:n], "log-normal"))
            self.p_pvalues.append(self.KS_testing(self.desc_data[:n], "pareto"))
            self.loading_bar(n)

    def loading_bar(self, n):
        # Maybe replace this with module.
        if n % (len(self.data) // 20) == 0:
                progress_percent = (n / len(self.data) * 100)
                filled_length = int(100 * progress_percent / 100)
                empty_length = 100 - filled_length
                loading_bar = '|' * filled_length + ' ' * empty_length
                print(f"{loading_bar} ({progress_percent:.0f}% done)")