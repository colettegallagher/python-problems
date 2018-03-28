# Colette Gallagher, 2018-03-25
# Exercise 6 Factorial
# https://en.wikipedia.org/wiki/Factorial
# https://www.youtube.com/watch?v=ZyYp1V84Xqc

# The factorial of a number is that number multiplied by all of the positive numbers less than it


def factorial(number):
    product = 1
    for i in range(number):
        product = product*(i+1)
    return product
# defines the function of the factorial


number = 5

int = number
factorial_of_int = factorial(int)
print("The factorial of", (int), "is ", (factorial_of_int))
# prints the factorial of the number 5 which equals 120

number = 7

int = number
factorial_of_int = factorial(int)
print("The factorial of", (int), "is ", (factorial_of_int))
# prints the factorial of the number 7 which equals 5040

number = 10

int = number
factorial_of_int = factorial(int)
print("The factorial of", (int), "is ", (factorial_of_int))
# prints the factorial of the number 10 which equals 3628800

