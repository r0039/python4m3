**Combining Lists: The Zip Function**

In Python, we have an assortment of built-in functions that allow us to build our programs faster and cleaner. One of those functions is zip().
The zip() function allows us to quickly combine associated data-sets without needing to rely on multi-dimensional lists

Notice two things:
* Our data set has been converted from a zip memory object to an actual list (denoted by [ ])
* Our inner lists don’t use square brackets [ ] around the values. This is because they have been converted into tuples (an immutable type of list).

```
owners = ["Jenny", "Alexus", "Sam", "Grace"]
dogs_names = ["Elphonse", "Dr. Doggy DDS", "Carter", "Ralph"]
owners_dogs_names = zip(owners, dogs_names)
print(owners_dogs_names)
convert_list = list(owners_dogs_names)
print(convert_list)
```
