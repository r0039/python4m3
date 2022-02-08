"""
The final boolean operator we will cover is not. This operator is straightforward: when applied to any boolean expression it reverses the boolean value. So if we have a True statement and apply a not operator we get a False statement.
>>>
not True == False
not False == True
<<<

Consider the following statement:
>>>
Oranges are not a fruit.
<<<

Here, we took the True statement oranges are a fruit and added a not operator to make the False statement oranges are not a fruit.
This example in English is slightly different from the way it would appear in Python because in Python we add the not operator to the very beginning of the statement. Let’s take a look at some of those:
>>>
not 1 + 1 == 2  # False
not 7 < 0       # True
<<<
"""

"""
Instruction:
Set the variables statement_one and statement_two equal to the results of the following boolean expressions:
Statement one:
>>>
not (4 + 5 <= 9)
<<<

Statement two:
>>>
not (8 * 2) != 20 - 4
<<<
"""
statement_one = not (4 + 5 <= 9)
print(statement_one)

statement_two = not (8 * 2) != 20 - 4
print(statement_two)

"""
The registrar’s office at Calvin Coolidge’s Cool College has been so impressed with your work so far that they have another task for you.
They want you to return to a previous if statement and add in several checks using and and not statements:

If a student’s credits is not greater or equal to 120, it should print:
>>>
"You do not have enough credits to graduate."
<<<

If their gpa is not greater or equal to 2.0, it should print:
>>>
"Your GPA is not high enough to graduate."
<<<

If their credits is not greater than or equal to 120 and their gpa is not greater than or equal to 2.0, it should print:
>>>
"You do not meet either requirement to graduate!"
<<<

Make sure your return value matches those strings exactly. Capitalization, punctuation, and spaces matter!
"""

credits = 120
gpa = 1.8

if not credits >= 120:
  print("You do not have enough credits to graduate.")

if not gpa >= 2.0:
  print("Your GPA is not high enough to graduate.")

if (not credits >= 120) and (not gpa >= 2.0):
  print("You do not meet either requirement to graduate!")
