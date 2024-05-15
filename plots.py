import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats

# Gets handed a pandas dataframe which is a single column of the population data.
### FIXME Issue 1: The POP column is not the same on each worksheet. ###
### Possible solution: Create a tuple value in the country_dictionary of (sheet_name, pop_column) ###
pop = 9
data = pd.read_excel(r'C:\Users\lconn\Documents\Programming\Python\Python Projects\Population_distribution\Data\EU_Census_2011_2016review.xlsx',
                     sheet_name='UK',
                     usecols=[pop])

# print(type(data))   <class 'pandas.core.frame.DataFrame'>

# Remove zero values
data = data.loc[(data!=0).any(axis=1)]   # axis 1 means this is applied to rows, axis 0 would be columns.
print("------------------------------------------------------------")
# CREATING HISTOGRAM
# Create histogram bins
print(data["POP"].max(axis=0))
print("------------------------------------------------------------")
### FIXME: correct the number of bins. 5 per order incriment?
bins = np.logspace(start=0, stop=np.log10(data["POP"].max(axis=0)), base=10)
midpoints = 0.5 * (bins[1:] + bins[:-1])
# Plot the histogram (Empirical distribution)
fig, axs = plt.subplots(1, 2)
axs[0].hist(data, bins=bins)

# Theoretical Log-normal distribution
log_data = np.log10(data)
lognorm_mean = log_data["POP"].mean()
lognorm_sd = log_data["POP"].std()
print(f"lognorm mean: {lognorm_mean}, lognorm sd: {lognorm_sd}")
x = np.linspace(lognorm_mean-3*lognorm_sd, lognorm_mean+3*lognorm_sd, 100)
y = stats.norm.pdf(x, lognorm_mean, lognorm_sd)
axs[1].plot(x, y)


plt.show()
