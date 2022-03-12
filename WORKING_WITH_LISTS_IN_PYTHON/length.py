"""
Often, we’ll need to find the number of items in a list, usually called its length.
We can do this using a built-in function called len().
When we apply len() to a list, we get the number of elements in that list:

my_list = [1, 2, 3, 4, 5]
print(len(my_list))

Would output:
5
"""

long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]
long_list_len = len(long_list)
print(long_list_len)
print()

big_range = range(2, 3000, 100)
print(list(big_range))
big_range_length = len(big_range)
print()
print(big_range_length)
