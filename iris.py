# Colette Gallagher, 19/03/18
# Excercise 5 Iris Data Set

print ("petal length ", "petal width ", "sepal length ", "sepal width")

with open ("data/iris.csv") as f:
  for line in f:
    print ("{:>10} {:>10} {:>10} {:>10}" .format(line.split(',')[0],line.split(',')[1],line.split(',')[2],line.split(',')[3]))
