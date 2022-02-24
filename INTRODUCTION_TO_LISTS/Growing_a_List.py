"""
Growing a List: Plus (+)

When we want to add multiple items to a list, we can use + to combine two lists (this is also known as concatenation).

Below, we have a list of items sold at a bakery called items_sold:
items_sold = ["cake", "cookie", "bread"]

Suppose the bakery wants to start selling "biscuit" and "tart":
items_sold_new = items_sold + ["biscuit", "tart"]
print(items_sold_new)

Would output:
['cake', 'cookie', 'bread', 'biscuit', 'tart']

In this example, we created a new variable, items_sold_new, which contained both the original items sold, and the new items. 
We can inspect the original items_sold and see that it did not change:
print(items_sold)

Would output:
['cake', 'cookie', 'bread']

We can only use + with other lists. If we type in this code:
my_list = [1, 2, 3]
my_list + 4

we will get the following error:
TypeError: can only concatenate list (not "int") to list

If we want to add a single element using +, we have to put it into a list with brackets ([]):
my_list + [4]
"""

orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:
new_orders = ["lilac", "iris"]

orders_combined = orders + new_orders
print(orders_combined)

broken_prices = [5, 3, 4, 5, 4] + [4]
print(broken_prices)

# TypeError
broken_prices = [5, 3, 4, 5, 4] + 4 

"""
Traceback (most recent call last):
  File "script.py", line 9, in <module>
    broken_prices = [5, 3, 4, 5, 4] + 4
TypeError: can only concatenate list (not "int") to list
"""
