In a `for` loop, we will know in advance how many times the loop will need to iterate because we will be working on a collection with a predefined length.

```
for <temporary variable> in <collection>:
  <action>
```

Let’s break down each of these components:

1. A `for` keyword indicates the start of a for loop.
2. A `<temporary variable>` that is used to represent the value of the element in the `collection` the loop is currently on.
3. An `in` keyword separates the `temporary variable` from the `collection` used for iteration.
4. A `<collection>` to loop over. In our examples, we will be using a list.
5. An `<action>` to do anything on each iteration of the loop.

**Example**
Let’s link these concepts back to our `ingredients` example. This `for` loop prints each `ingredient` in `ingredients`:

```
ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]
 
for ingredient in ingredients:
  print(ingredient)
```

In this example:

* `ingredient` is the `<temporary variable>`.
* `ingredients` is our `<collection>`.
* `print(ingredient)` was the `<action>` performed on every iteration using the temporary variable of ingredient.

**Some things to note about for loops:**
**Temporary Variables:**
A temporary variable’s name is arbitrary and does not need to be defined beforehand. Both of the following code snippets do the exact same thing as our above example:
```
for i in ingredients:
  print(i)
```
or
```
for item in ingredients:
 print(item)
```

Programming best practices suggest we make our temporary variables as descriptive as possible. Since each iteration (step) of our loop is accessing an ingredient it makes more sense to call our temporary variable `ingredient` rather than `i` or `item`.

**Indentation:**
Notice that in all of these examples the print statement is indented. Everything at the same level of indentation after the for loop declaration is included in the loop body and is run on every iteration of the loop.
```
for ingredient in ingredients:
  # Any code at this level of indentation 
  # will run on each iteration of the loop
  print(ingredient)
```

If we ever forget to indent, we’ll get an `IndentationError` or unexpected behavior.

**Elegant loops:**
Python loves to help us write elegant code so it allows us to write simple `for` loops in one-line. In order to see the below example as one line, you may need to expand your narrative window. Here is the previous example in a single line:
```
for ingredient in ingredients: print(ingredient)
```

Note: One-line for loops are useful for simple programs. It is not recommended you write one-line loops for any loop that has to perform multiple complex actions on each iteration. Doing so will hurt the readability of your code and may ultimately lead to buggier code.

