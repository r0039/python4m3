"""
What if we want to select the last element of a list?

We can use the index -1 to select the last item of a list, even when we don’t know how many elements are in a list.

Consider the following list with 6 elements:
pancake_recipe = ["eggs", "flour", "butter", "milk", "sugar", "love"]

If we select the -1 index, we get the final element, "love".
print(pancake_recipe[-1])

Would output:
love

This is equivalent to selecting the element with index 5:
print(pancake_recipe[5])

Would output:
love

Here are the negative index numbers for our list:

Element	Index
"eggs"	-6
"flour"	-5
"butter"	-4
"milk"	-3
"sugar"	-2
"love"	-1
"""

shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]

last_element = shopping_list[-1]
print(last_element)

index5_element = shopping_list[5]
print(index5_element)
