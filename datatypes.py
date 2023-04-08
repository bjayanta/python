"""
Built-in Data Types:

Text Type:	        str
Numeric Types:	    int, float, complex
Sequence Types:	    list, tuple, range
Mapping Type:	    dict
Set Types:	        set, frozenset
Boolean Type:	    bool
Binary Types:	    bytes, bytearray, memoryview
None Type:	        NoneType
"""

"""
Getting the Data Type:
Get the data type of any object by using the type() function.
In Python, the data type is set when you assign a value to a variable.
Example:
"""
print(type(10)) # Integer
print(type(10.5)) # Float
print(type(1j)) # Complex
print(type('Jayanta')) # String
print(type(True)) # Boolean
print(type(["apple", "banana", "cherry"])) # List
print(type(("apple", "banana", "cherry"))) # Tuple
print(type(range(6))) # Range
print(type({"name" : "John", "age" : 36})) # Dictionary
print(type({"apple", "banana", "cherry"})) # Set
print(type(frozenset({"apple", "banana", "cherry"}))) # Frozenset
print(type(b"Hello")) # Bytes
print(type(bytearray(5))) # Bytearray
print(type(memoryview(bytes(5)))) # Memoryview
print(type(None)) # NoneType

"""
Setting the Specific Data Type:
If you want to specify the data type, you can use the following constructor functions.
Example:
"""

x = str("Hello World") # String	
x = int(20)	# Integer	
x = float(20.5)	# Float	
x = complex(1j)	# Complex	
x = list(("apple", "banana", "cherry"))	# List	
x = tuple(("apple", "banana", "cherry")) # Tuple	
x = range(6) # Range	
x = dict(name="Jayanta", age=36) # Dictionary
x = set(("apple", "banana", "cherry")) # Set
x = frozenset(("apple", "banana", "cherry")) # Frozenset	
x = bool(5) # Boolean	
x = bytes(5) # Bytes	
x = bytearray(5) # Bytearray	
x = memoryview(bytes(5)) # Memoryview