suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# We wanted to slice the first three elements.
print(suitcase[:3])
print()

# We want to slice the last n elements in a list.
print(suitcase[-3:])
# Your code below: 
print()
# Negative indices can also accomplish taking all but n last elements of a list.
print(suitcase[:-3])

last_two_elements = suitcase[-2:]
print(last_two_elements)
print()

slice_off_last_three = suitcase[:-2]
print(slice_off_last_three)
