"""
By default, range() creates a list starting at 0. However, if we call range() with two inputs, we can create a list that starts at a different number.
"""

"""
Modify the range() function that created the range range_five_three such that it:
* Starts at 5
* Has a difference of 3 between each item
* Ends before 15
"""
range_five_three = range(5, 15, 3)
print(list(range_five_three))
print()

"""
Create a range called range_diff_five that:
* Starts at 0
* Has a difference of 5 between each item
* Ends before 40
"""
range_diff_five = range(0, 40, 5)
print(list(range_diff_five))
