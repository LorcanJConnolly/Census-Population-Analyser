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
# ==============================================================================================================
# Remove zero values
data = data.loc[(data!=0).any(axis=1)]   # axis 1 means this is applied to rows, axis 0 would be columns.
log_data = np.log10(data)
### FIXME remove null values. 
# ==============================================================================================================
# CREATING HISTOGRAM
fig, axs = plt.subplots(1, 5)
# Create histogram bins
### FIXME Issue 2: correct the number of bins. 5 per order incriment?
bins = np.logspace(start=0, stop=np.log10(data["POP"].max(axis=0))+1, base=10)
# Plot the histogram (Empirical distribution)
vals, _, _ = axs[0].hist(data, bins=bins)
# Plot midpoints
#### FIXME: plot and join midpoints.
midpoints = 0.5 * (bins[1:] + bins[:-1])
axs[0].plot(midpoints, vals, c='green')
axs[0].set_xscale('log')   # log scale the x axis
# ==============================================================================================================
# Theoretical Log-normal distribution
mu = log_data["POP"].mean()
s = log_data["POP"].std()
### FIXME: variable names
x = np.linspace(0, log_data["POP"].max()+1, 100)
y = stats.norm.pdf(x, loc=mu, scale=s)
axs[1].plot(x, y, c='red')
# ==============================================================================================================
# Histogram plot with log data
### WORKS AS INTENDED ###
### FIXME: add the counts axis to the right size of the plot. ###
log_bins = np.arange(0, log_data["POP"].max()+1, 0.05)
axs[4].hist(log_data, bins=log_bins)
axs[3].hist(log_data, bins=log_bins, density=True)   # Area under the curve = 1, like a pdf.
axs[3].plot(x, y, c='red')
# ==============================================================================================================
plt.show()
