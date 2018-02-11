# Colette Gallagher, 2018-02-11
# URL: https://en.wikipedia.org/wiki/Collatz_conjecture

n = 17
while n > 1:
  if n % 2==0:
    n = n / 2
  else: 
    n = 3 * n + 1
  print (n)
