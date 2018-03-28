# Colette Gallagher, 2018-03-19
# Exercise 5 Iris Data Set
# https://docs.python.org/2/library/string.html

print ("petal length ", "petal width ", "sepal length ", "sepal width")
# Prints the Iris Dataset header names 

with open ("data/iris.csv") as f:
# Opens the iris data set which must be saved as a .csv file on visual studio code, link in comment box

  for line in f:
    print ("{:>10} {:>10} {:>10} {:>10}" .format(line.split(',')[0],line.split(',')[1],line.split(',')[2],line.split(',')[3]))
# Splits the string and formats each entry into tabular format
