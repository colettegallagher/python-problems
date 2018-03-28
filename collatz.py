# Colette Gallagher, 2018-02-11
# URL: https://en.wikipedia.org/wiki/Collatz_conjecture
# https://stackoverflow.com/questions/33508034/making-a-collatz-program-automate-the-boring-stuff

n = 17
# Starting integer is 17

while n > 1:
  if n % 2==0:
    n = n / 2
# Divide by 2 if the integer is Even

  else: 
    n = 3 * n + 1
# Multiple by 3 and add 1 if the integer is Odd

  print (n)
# Print at each iteration
