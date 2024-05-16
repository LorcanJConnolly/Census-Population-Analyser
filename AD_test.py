### The Kolmogorov–Smirnov statistic quantifies a distance between the empirical distribution function of the sample and the cumulative distribution function of the reference distribution (Lognormal/Parento).
### The null distribution of this statistic is calculated under the null hypothesis that the sample is drawn from the reference distribution (in the one-sample case).



### the test is less powerful for testing normality than the Shapiro–Wilk test or Anderson–Darling test.

### It only applies to continuous distributions.
### It tends to be more sensitive near the center of the distribution than at the tails.
### Perhaps the most serious limitation is that the distribution must be fully specified. That is, if location, scale, and shape parameters are estimated from the data, the critical region of the K-S test is no longer valid. It typically must be determined by simulation.


### Try the Anderson-Darling test.
### https://www.itl.nist.gov/div898/handbook/eda/section3/eda35e.htm
### Its just: scipy.stats.anderson(log_data, dist='norm')