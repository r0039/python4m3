**Name Errors**. 

A `NameError` is reported by the Python interpreter when it detects a variable that is unknown.

This can occur if a variable is used before it has been assigned a value or if a variable name is spelled differently than the point at which it was defined. 
The Python interpreter will display the line of code where the `NameError` was detected and indicate which name is found that was not defined.

Here’s an example of a `NameError` error message:
```
File "script.py", line 1, in <module>
    print(score)
NameError: name 'score' is not defined
```

This error is suggesting that the variable score was never defined in the program. Oops.

Some common name errors are:

* Misspelling a variable name.
* Forgetting to define a variable.
