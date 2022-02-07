"""Often, the conditions you want to check in your conditional statement will require more than one boolean expression to cover. In these cases, you can build larger boolean expressions using boolean operators. These operators (also known as logical operators) combine smaller boolean expressions into larger boolean expressions.

There are three boolean operators that we will cover:

* and
* or
* not

Let’s start with and.
and combines two boolean expressions and evaluates as True if both its components are True, but False otherwise.

Consider the example:

Oranges are a fruit and carrots are a vegetable.
This boolean expression is comprised of two smaller expressions, oranges are a fruit and carrots are a vegetable, both of which are True and connected by the boolean operator and, so the entire expression is True.

Let’s look at an example of some AND statements in Python:

(1 + 1 == 2) and (2 + 2 == 4)   # True
 
(1 > 9) and (5 != 6)            # False
 
(1 + 1 == 2) and (2 < 1)        # False
 
(0 == 10) and (1 + 1 == 1)      # False
Notice that in the second and third examples, even though part of the expression is True, the entire expression as a whole is False because the other statement is False. The fourth statement is also False because both components are False."""

statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)
print(statement_one)

statement_two = (4 * 2 <= 8) and (7 - 1 == 6)
print(statement_two)

credits = 120
gpa = 3.4

if credits >= 120 and gpa >= 2.0:
  print("You meet the requirements to graduate!")
