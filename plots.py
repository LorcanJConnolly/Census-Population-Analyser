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
# CREATING HISTOGRAM
# Create histogram bins
### FIXME Issue 2: correct the number of bins. 5 per order incriment?
bins = np.logspace(start=0, stop=np.log10(data["POP"].max(axis=0))+1, base=10)
# Plot the histogram (Empirical distribution)
fig, axs = plt.subplots(1, 4)
vals, _, _ = axs[0].hist(data, bins=bins)
# Plot midpoints
midpoints = 0.5 * (bins[1:] + bins[:-1])
axs[0].plot(midpoints, vals, c='green')
axs[0].set_xscale('log')   # log scale the x axis

# Theoretical Log-normal distribution
log_data = np.log10(data)
mu = log_data["POP"].mean()
s = log_data["POP"].std()
### FIXME Issue 4: x scale on plot1 goes from 0-10**5, plot2 goes from 0-5
### Potential solution: would it be easier to also plot the historgam using log_data
x = np.linspace(0, log_data["POP"].max()+1, 100)
### FIXME Issue 3: y values are scaled down, wrong values.
### Area of bin * number of samples
y = stats.norm.pdf(x, loc=mu, scale=s)
axs[1].plot(x, y, c='red')
y=y*log_data["POP"].sum()  # attempt at pdf to frequency scaling
axs[2].plot(x, y, c='red')

# attempt at twinx plot
axs2 = axs[3].twinx()
axs[3].plot(midpoints, vals, c='orange')
axs2.plot(x, y, c='red')
axs2.set_box_aspect(1)

plt.show()
