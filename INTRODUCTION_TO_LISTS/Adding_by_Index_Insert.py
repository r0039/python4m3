"""
The Python list method .insert() allows us to add an element to a specific index in a list.

The .insert() method takes in two inputs:

The index you want to insert into.
The element you want to insert at the specified index.
The .insert() method will handle shifting over elements and can be used with negative indices.
"""
front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

# Your code below: 
front_display_list.insert(0, "Pineapple")
print(front_display_list)

front_display_list.insert(1, "Pototo")
print(front_display_list)

# negative indices
front_display_list.insert(-2, "Hola")
print(front_display_list)
