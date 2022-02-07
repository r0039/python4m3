"""
The boolean operator or combines two expressions into a larger expression that is True if either component is True.

Consider the statement

Oranges are a fruit or apples are a vegetable.
This statement is composed of two expressions: oranges are a fruit which is True and apples are a vegetable which is False. Because the two expressions are connected by the or operator, the entire statement is True. Only one component needs to be True for an or statement to be True.

In English, or implies that if one component is True, then the other component must be False. This is not true in Python. If an or statement has two True components, it is also True.

Let’s take a look at a couple of examples in Python:

True or (3 + 4 == 7)    # True
(1 - 1 == 0) or False   # True
(2 < 0) or True         # True
(3 == 8) or (3 > 4)     # False
Notice that each or statement that has at least one True component is True, but the final statement has two False components, so it is False.
"""

statement_one = (2 - 1 > 3) or (-5 * 2 == -10)
print(statement_one)

statement_two = (9 + 5 <= 15) or (7 != 4 + 3)
print(statement_two)

credits = 118
gpa = 2.0

if (credits >= 120) or (gpa >= 2.0):
  print("You have met at least one of the requirements.")

