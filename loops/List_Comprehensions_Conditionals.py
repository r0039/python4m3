# We have defined a list heights of visitors to a theme park. 
# In order to ride the Topsy Turvy Tumbletron roller coaster, you need to be above 161 centimeters.

Using a list comprehension, create a new list called can_ride_coaster that has every element from heights that is greater than 161.
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [num for num in heights if num > 161]
print(can_ride_coaster)

# Example 1:
numbers = [2, -1, 79, 33, -45]
only_negative_doubled = []
 
for num in numbers:
  if num < 0: 
    only_negative_doubled.append(num * 2)
 
print(only_negative_doubled) 

# Example 2:
numbers = [2, -1, 79, 33, -45]
negative_doubled = [num * 2 for num in numbers if num < 0]
print(negative_doubled)

# Example 3:
numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 if num < 0 else num * 3 for num in numbers ]
print(doubled)
