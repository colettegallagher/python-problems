# Colette Gallagher, 2018-03-25
# Exercise 6 Factorial
# https://en.wikipedia.org/wiki/Factorial
# https://www.youtube.com/watch?v=ZyYp1V84Xqc
# https://nbviewer.jupyter.org/github/ianmcloughlin/python-fundamentals-notes/blob/master/functions-modules.ipynb#

# The factorial of a number is that number multiplied by all of the positive numbers less than that number


def factorial(n):
# Returns the factorial of n
    ans = 1
    for i in range(2, n + 1):
        ans = ans * i
    return ans
# defines the function of the factorial

x=5
y=7
z=10
# Gives values to x,y,z

print("The Factorial of", (x), "is ", factorial(x))
print("The Factorial of", (y), "is ", factorial(y))
print("The Factorial of", (z), "is ", factorial(z))  
# Prints the Factorials of the numbers 5, 7, 10 to give the factorials 120, 5040, 3628800 respectively


