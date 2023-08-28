# PYTHON EXCEPTIONS

-An exception is an event that occurs during the execution of a program that interupts the normal flow
-When a python script encounters an event it cannot cope with, it must have ways to handle
-When a python script raises an exception, it must either handle the exception immediately of terminate the program
# Handling exception
- When you are handling suspicious code that may raise an exception you can defend your code using a `try` block.
- After the `try` block, you include an `except` statement followed by a block of code that handles the exception
 ### syntax
 ```python
try:
	# do you operation here, code you want to monitor for errors
except exception1:
	#if there is exception 1, execute this block
except exception 2:
	#if there is exception 2, execute this block
else:
	#if there is no exception, execute this block
finally:
	#code that will run wether an exception was raised or not
```

- A single `try` statement can have multiple `except` statements, useful for a try statement that might through a couple of exceptions
- The `else` block contains code that doesn't require the `try` blocks protection
```python

  1 #!/usr/bin/python3
  2
  3 try:
  4 →   x = int(input("enter a number: "))
  5 →   result = 10/x
  6 except ZeroDivisionError as zde: #this will be run if a user provide 0 as input
  7     print("Error: Division by zero")
  8 except ValueError as ve: #this will run if the user provide a negative value as input
  9     print("Error: Invalid input")
 10 else:
 11     print("Result:", result)
```

### example 2 :
- Opens a file, writes content into it and come out gracefully
```python
#!/usr/bin/python3

try:
	fh = open("testfile", "w")
	fh.write("This is my text file for exception handling!")
except IOError:
	print "Error: cannot find file ore read data"
else:
	print "Written content to the file successfully"
	fh.close()
	```

### Example 3
```python
try:
	fh = open=("testfile", "w")
	fh.write("This is my test file for exception handling")
except IOError:
	print ("Error: can\t find file or read data")
else:
	print("Written content in the file successfully")
	fh.close()

```

### Example 4:
-Tries to open a file wherr you do not have written permission, so it raises an exception

```python
#!/usr/bin/python3

python:
	fh = open("textfile", "r")
	fh.write("This is my testfile for exception handlin")
except:
	print("Error: can\t find file or read data")
else:
	print ("Written  content in the file successfully")
```

# The `except` clause with No Exceptions
-It is possible to use the `except` statement without the exceptions
-this is not considered as good programming practise as it catches all the exceptions but does not make the programmer identify the root cause of the problem that may occur.

## syntax
```python
try:
	your operation
except:
	If there is any exception, excecute this block
else:
	#if there is no exception, execute this
	```

## `except` with multiple Exception
## syntax
```python
try:
	#You do your operations
except (exception1[exception2[exception3[]]]):
	#if there is any exception from the given list, execute this block
else:
	#if there is no exception, execute this block
	```

- To ignore any exceptions, use the `pass` key word
```python

try:
	print(10/0)
except:
	pass
```

You can explicitly speicify the error or create a variable with the `as` keyword to print the default error

```python
try:
	print(10/0)
except ZeroDivisionError as e
	print(e) #this prints the default error message
```


