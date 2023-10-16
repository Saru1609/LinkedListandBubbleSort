def fibonacci(n):
  a, b = 0, 1
  for i in range(n):
    a, b = b, a+b
  return a

# Generate the first ten numbers in the Fibonacci series
for i in range(10):
  print(fibonacci(i))

