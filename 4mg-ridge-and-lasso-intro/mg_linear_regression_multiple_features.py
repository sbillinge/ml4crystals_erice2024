# First do the waves_problem below.  We will fit waves data from MG first using the LineraRegression model in sklearn
# and then using the K-nearest neighbors model
#
# Whenever you see a colon ":" type your code after that.  You can run the code from your IDE if it is set up,  or
# from the command line by typing `python mg_linear_regression.py` with `waves_problem()` uncommented in the `if __name__`
# section at the bottom of this file.

from mg_linear_regression import plot_sloping_line
import mglearn

import matplotlib.pyplot as plt
import numpy as np


def multi_dimensional_linear_regression():

    # make your own example similar to the waves_problem linear regression example in
    # mg_linear_regressor, except for the Boston Housing dataset.  Load the data from sklearn and
    # also the extended data from mglearn.

    # The previous example introduced the linear regression on a system that had a single feature
    # that had a linear dependence on an independent variable.  This introduces linear regression
    # in a familiar way to physical scientists.  In this edex we want to demonstrate how complex
    # problems can be studied with linear models.  This is still largely from Chapter 2 of Muller
    # and Guido but now you have to make the story in a way where
    #       1. the data are loaded and investigated by printing and plotting to gain insight
    #       2. discuss the features and labels and what they mean
    #       3. write prompts and then the code to execute after that compare the results from
    #          straight linear regressions, ridge regression and Lasso
    #       4. discuss how and what you learn about your data from the different models, and compare
    #          their performance

    return


if __name__ == '__main__':
    multi_dimensional_linear_regression()
    plt.show()
