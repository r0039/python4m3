"""
Python gives us an easy way of creating these types of lists using a built-in function called range().
The function range() takes a single input, and generates numbers starting at 0 and ending at the number before the input.
So, if we want the numbers from 0 through 9, we use range(10) because 10 is 1 greater than 9:

my_range = range(10)
print(my_range)

Would output:
range(0, 10)

Notice something different? The range() function is unique in that it creates a range object. It is not a typical list like the ones we have been working with.
In order to use this object as a list, we have to first convert it using another built-in function called list().
The list() function takes in a single input for the object you want to convert.
"""

# Your code below: 

number_list = range(9)
print(number_list)
print(list(number_list))

zero_to_seven = range(8)
print(list(zero_to_seven))
