### dist_test
    # def build_sample
        # returns a sample which is a slice of the data that is one larger than the previous slice.
    # def KS_testing
        # calculates the fitted parameters of the LN and P distrubiotn of the data
        # creates a cdf from these parameters
        # creates the ecdf from the data (a step function).
        # preforms a KS test comparing the ecdf to the cdf
        # returns the p-value from the result
    # def goodness_of_fit_testing
        # calls KS_testing twice with the sample, once for the LN and once for the P distribution.
        # calls build_sample with the sample to generate the new sample
        # checks if the new sample is the entire parent data set
        # if it is stops, if it is not recursively calls goodness_of_fit_testing with the sample.
    # def plotting
        