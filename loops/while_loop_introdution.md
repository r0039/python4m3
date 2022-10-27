In Python, `for` loops are not the only type of loops we can use. Another type of loop is called a while loop and is a form of indefinite iteration.
A `while` loop performs a set of instructions as long as a given condition is `true`.

```
while <conditional statement>:
  <action>
```

Let’s examine this example, where we print the integers `0` through `3`:
```
count = 0
while count <= 3:
  # Loop Body
  print(count)
  count += 1
```

Note the following about `while` loops before we write our own:
**Indentation:**
Similar to a `for` loop, everything at the same level of indentation after the `while` loop declaration is run on every iteration of the loop while the condition is true.
```
while count <= 3:
  # Loop Body
  print(count)
  count += 1
  # Any other code at this level of indentation will
  # run on each iteration
```
If we ever forget to indent, we’ll get an `IndentationError` or unexpected behavior.

**Elegant loops:**
Similar to `for` loops, Python allows us to write elegant one-line `while` loops. Here is our previous example in a single line:
```
count = 0
while count <= 3: print(count); count += 1
```

Note: Here we separate each statement with a ; to denote a separate line of code.
