from dist_test import Population_Dist_Tester
from animation_plotter import Animation

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

from matplotlib.animation import FuncAnimation

df = np.load(r'C:\Users\lconn\Documents\Programming\Python\Python Projects\Population_distribution\Pop_distribution_analyser\Numpy_Arrays/UK_array.npy')

if __name__ == "__main__":
    data = Population_Dist_Tester(df)
    data.goodness_of_fit_testing()
    print(data.desc_data[0], data.desc_data[-1])
    ani = Animation(xdata=data.desc_data, ydata=data.ln_pvalues)
    ani.run()