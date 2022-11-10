# What if we want to print out all of the numbers in a list, but only if they are positive integers. 
# We can use another common loop control statement called continue.

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
for i in ages:
  if i < 21:
    continue
  print(i)
