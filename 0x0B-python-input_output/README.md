- `open()` returns a file object. it takes two positional arguments and one keyword argument.
`open('workfile', 'w', encoding="utf-8")`

```python
>>> open('workfile', 'w', encoding="utf-8")

```

-The first argument is a string containing the filename
-The second argument is a string containing a few characters describing the way in which the file will be used.
`r` - read only mode
`w` - write only mode -existing file with the same name will be errased
`a` - append file
`r+` - opens the file for both reading and writting
`b` - opens the file in binary mode where data is written and read as bytes object
NB: the mode argumet is optional and if excluded, the `r` is assumed
- Files are read and writen in text mode which are endoded in  a specific encoding.
- If encoding is not specified, the default encoding is platform depended
- `encoding="utf-8"` is is recommended unless otherwise becaue its the mordern  defacto standard
- You cannot specify encoding when opening the file in binay mode
- It is adviceable to use the `with` keyword when working with files
- The advantage is that the file is properly closed after its operations end
```python

>>>with open('workfile', encoding="utf-8") as f:
			read_data = f.read()
>>># we can check if the file was automaticaly closed
>>>f.closed
True
```

- When not using the `with` keyword, you should call the `f.close()` to close the file and immediately free up any resources used by 
it.
NB: calling `f.write()` without using `with` or calling `f.close()` might result in arguments of `f.write()` not being  completely written to the disk even if the program exists successfully.
- A file can either be close by `with` which does it automatic or by calling `f.close()`. 
- Any attempts to use the file after it has been closed will fail
```
>>> f.close()

>>> f.read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file
