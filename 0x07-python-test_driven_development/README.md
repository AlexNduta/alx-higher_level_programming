# TEST DRIVEN DEVELOPMENT
###  never trust the user, always think of possible edge cases

 `test` folder contain all test files with `.txt` extension
 our root diectory containts all our code files
# Requirements
 - the first line of our code should always be `#!/usr/bin/python3`
 - All files must be executable
 - The length of the files are tested using `wc` 


# Tests
- All tests should be executed using the command `python3 -m doctest ./tests/*`
- All modules should have a documentattion `python3 -c 'print(__import("my_module").__doc__)
- All functions should have a documentation `python3 'print(__import__("my_module").my_function.__doc__)'
