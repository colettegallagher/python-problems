# Colette Gallagher, 2018-02-28
# https://projecteuler.net/problem=5
# https://stackoverflow.com/questions/8024911/project-euler-5-in-python-how-can-i-optimize-my-solution

def check(n):
    for i in range(11, 21):
# use only numbers 11 to 20 as we know 2520 is the smallest number divided by 1 to 10  

        if n % i == 0:
            continue
        else:
            return False
    return True
    
x = 2520
 # we know 2520 is the smallest number that can be divided by 1 to 10 so we can start from 2520 to shorten the calculation time
    
while not check(x):
    x += 2520
   
print(x)
