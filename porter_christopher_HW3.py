# -*- coding: utf-8 -*-
"""
This program is Python HW 3 Group C & D in Math 510.  There are six questions 
answered below.

Before beginning the questions two libraries are imported.

The pandas library which is used for dataframe analytics
The matplotlib.pyplot library is used for plotting histograms.

ctp Fall 2016
"""


import pandas as pd
import matplotlib.pyplot as plt    

# 1.)
'''
This answer imports the IRIS dataset from the UCI Machine Learning 
repository. Pandas read_csv method is used to read the csv from a URL. 
First, a header file is read in to create a list of column headers for 
the iris data.

Note: no .header file was found online.  Instead I created a local csv
file with the column names written in them. This demonstrates a different way
to read a file into memory, but it is instead located on the local machine.

I will submit this file along with the homework.


'''
fileReader = open('iris_header.csv') # Open the iris header file and save as fileReader

for row in fileReader:       # loop through the rows in the csv file (there is only one in a typical .header)
    headerList = row.split(',')  # for each row create a list of each item (the column names)
    n = 0 # initialize an iterator
    for elem in headerList:  # loop through each element in the headerList
        headerList[n] = elem.strip()         # strip the elements of any leading or trailing whitespace
        n += 1    # iterate
        
df = pd.read_csv('http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', 
                 header=None, names = headerList, index_col = False) # use pand.read_csv to import the csv file located in the 
                                             # specified URL (the UCI machine learning data). indicate that there are no
                                             # column names so that the data begins in the first line.  Use the headerList
                                             # to name the colmns, and do not use the first columns as the dataFrame index.
                                             # the result is a dataframe with the sepal & petal's length & width, and a class
                                             # variable


 # 2.)
'''
This answer uses the head and tail method of a pandas dataframe to 
the first and last ten rows of the dataframe created in problem 1.
'''
print(df.head(10))  # a panda dataframe object has the method 'head' which prints the n first rows of the dataframe

print(df.tail(10)) # like heads, but last n rows of the dataframe



# 3.)
'''
This answer uses the describe method in a pandas dataframe to display the
the count, Mean, STD, Min, 25%, 50%, 75% and MAX statistics of each varible
in the dataframe created in step 1.
'''
print(df.describe())  # the describe method for a pandas dataframe provides the count, Mean, STD, Min, 25%, 50%, 75% and MAX. 


#4.)
'''
This answer writes a function that accepts a list of numbers that represent numbers of bins and, using 
Pandas, plots a histogram for each of the numeric columns at each bin size. 
The histograms is grouped  by the column name.
'''
def histo_iris(bins):
    '''
    This function accepts a list of integers that indicate the number of bins to 
    use for a set of histograms on for the iris dataset.  The resulting plot
    will be a set of n x 4 histgorams, where n is the number of integers in the 
    bins list, and 4 is the number of numeric variables in the iris
    dataset.  The histograms will be groupd by each metric.
    
    Parameters:
    bins - a list, containing integers, that indicate the number of bins to use 
    for each histogram.
    
    ctp - Fall 2016 
    '''
    fig, axs =  plt.subplots(4, 3)      # using the matplotlib.pyplot library
                                        # create a figure consisting of subplots
                                        # made up of 4 by 3 figures    
    
    axs = axs.ravel()                   # use the ravel method to flatten the list axs created in the previous line
        
    n = 0  # intialize an iterator
    
    for col in df:         # loop through each column in the dataframe
        for b in bins:     # loop through each bin size in the bins list
            if n > 11:     # ensure only 12  plots are created
                break      # exit the loop on the 13th iteration
            else:          # Otherwise,
                axs[n].hist(df[col], bins = b)  # create a histogram of b bins, for the column in the dataframe
                                                # on the nth axis
                n += 1                          # iterate
            
    return fig      # return the figure

bins = [10, 50, 100]  # the example bin list
histo_iris(bins) # test the function



#5.)
'''
This is an answer to question five, which asks to plot a boxplot for the 4 numeric columns
'''
df.plot.box()   # use the plot.box method of a pandas dataframe object to creae a boxplot of each numeric variable



#6.)
'''
This is an answer to question six, which asks to plot a barchart for the nominal column
It was not clear on what metric of the data was meant to be plotted, therefore I chose
to plot the average of each numeric variable by the class variable.

I could have done the count (which is 50, and uninteresting, or many stats using the describe method.
'''
barDF = df.groupby('classes').mean()

barDF.plot.bar()

# df.plot.bar()