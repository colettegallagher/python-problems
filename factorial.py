# Colette Gallagher, 2018-03-25
# Exercise 6 Factorial
#https://www.youtube.com/watch?v=ZyYp1V84Xqc


def factorial(number):
    product = 1
    for i in range(number):
        product = product*(i+1)
    return product

number = 5

int = number
factorial_of_int = factorial(int)
print("The factorial of", (int), "is ", (factorial_of_int))

number = 7

int = number
factorial_of_int = factorial(int)
print("The factorial of", (int), "is ", (factorial_of_int))

number = 10

int = number
factorial_of_int = factorial(int)
print("The factorial of", (int), "is ", (factorial_of_int))


