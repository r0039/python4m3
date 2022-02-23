"""
For lists, methods will follow the form of list_name.method(). Some methods will require an input value that will go between the parenthesis of the method ( ).

An example of a popular list method is .append(), which allows us to add an element to the end of a list.

append_example = [ 'This', 'is', 'an', 'example']
append_example.append('list')
print(append_example)

will output:
['This', 'is', 'an', 'example', 'list']
"""

example_list = [1, 2, 3, 4]

# Append only add one value, not multiple. 
#Using Append
example_list.append(5)
print(example_list)

#Using Remove
example_list.remove(5)
print(example_list)

 
