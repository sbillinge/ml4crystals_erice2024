# The purpose of this is to show students how to reuse cused without using cut and paste.
#
# The exercise starts with some code from MG chapter 2 exercises that loads data and plots it and then trains
# a linear regression model and then plots the result.  Code for plotting the straight line is inline in the code.
#
#
#      1. make the code to plot a straight line reusable by defining a function within the same script
#      2. make the code reusable in multiple modules in the same project by putting it into another module in
#        the same directory and then successfully importing it
#      3. finally, if it is to be shared across projects, make a small minimal package somewhere, crete a minimimal
#        pyproject.toml file and then use pip install -e . to get it into the current virtual env and rerun the script

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

import mglearn
from ml4ms.shared_code.plot_helpers import plot_straight_line

def waves_problem():
    # import the make_wave dataset from the Muller-Guido package
    X, y = mglearn.datasets.make_wave(n_samples=60)

    # Get to know the data.  just print it:
    xvec = X.T[0,:]
    print(X.T[0,:])
    print(y)


    # Now we know the shape etc., let's plot it.
    # Make any mods to the data type or shape you need to make this work.
    # After those mods, as a sanity check, print the lengths of them:

    # ok, let's plot the data to see what it looks like:
    plt.plot(xvec,y,'o')

    # It looked like noisy data with a kind of upward trend to the right.
    # As materials scientists we may want to fit a line to this data. The
    # simplest line would be linear.  We could use lmfit, sccipy.optimize, or
    # diffpy.cmi for example.
    # if we use scikit learn, the logic is a bit different.  We assume that
    # there is a linear model underlying the data, y=mx + c, and we are
    # randomly making samples of some measurement that has this behavior.  using
    # the linear regressor in sklearn will take one x-point and predict the
    # y-value given m and b that it learns by sampling a  bunch of times.

    # Create the test and train data-sets (of samples):
    X_train, X_test, y_train, y_test = train_test_split(X,y)

    # instantiate the model the LinearRegression() model from sklearn into a variable called lr:
    lr = LinearRegression().fit(X_train, y_train)

    # do the training on the training set:

    # lr is now a trained model and has estimates for m and c but how do we
    # access those?  let's figure out what the attributes of lr are. We can do that by printing the model
    # attribute `lr.__dict__` or using the dict method `dict(lr)`:
    print(lr.__dict__)
    print(lr.n_jobs)

    # from this we can guess it puts m in "coef_" and c in "intercept_".  Print the m and c that it found from the
    # training:
    slope = lr.coef_
    intercept = lr.intercept_

    # Replot the data, but this time also the line on top.  You can use the  `plot_sloping_line()` to help if you like:
    straight_line_plot = plot_straight_line(xvec, slope, intercept)

    # In materials science we often just want to know m and c because it is
    # some physics or chemistry we are after.  In ML, we are often more
    # interested in the knowing how well the model will predict future data.
    # for example, we can ask the model to predict the y-values for the test data.
    # Get predictions for the test data from the trained model:


    # Add the predictions to our plot using a different color.
    # Also, Add the actual values of those points with another symbol:


    # And we can score how well the model did at predicting.  The score is the
    # R^2 value.  Print the score for the trained model against the training data
    # and against the testing data:
    # print(f"ls R^2 for training data: {}")


    # OK. if we want to use the ML to predict new values we can take another
    # approach.  We can use the KNN approach, similar to the irises example, but
    # using it for regression not for classification.
    # Let's create a new Figure so when we show the plots a new one pops up
    # fig2 = plt.figure()

    # instantiate the KNeighborsRegressor model selecting 1 neighbor and put it in a
    # variable k1n and train it (try doing it in one line this time:

    # print the R^2 for the training and testing data:

    # extract model predictions for the test data and plot them on top of the actual data using different symbols and colors:

    # As well as making predictions on a test set, we can make any array of points on our domain axis and make predictions
    # on them.  Make a grid of 1000 points that goes from the minimum to the maximum value of our dataset.
    # Have the model predict on each of those points and make a plot where these predictions are plotted as a line through
    # the known points:

    # now we will play with the number of neighbors and see what happens.
    # make a for loop that instantiates KNN models for 1, 3, 5, 7, 9, 11 neighbors, prints the R^2 score for each case on the
    # the training and testing data and creates a figure that is a 3x3 grid of subplots that looks like figure above
    # for each case, the actual data and the line through it from the predictions on a dense grid:




if __name__ == '__main__':
    waves_problem()
    plt.show()
