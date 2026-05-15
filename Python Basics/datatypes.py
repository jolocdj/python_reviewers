# Data Types 
# Built-in Data Types
# 1. Numeric Types: int, float, complex
# 2. Sequence Types: list, tuple, range
# 3. Text Type: str
# 4. Mapping Type: dict
# 5. Set Types: set, frozenset
# 6. Boolean Type: bool
# 7. Binary Types: bytes, bytearray, memoryview

# Numeric Types
x = 5           # integer
y = 3.14        # float
z = 2 + 3j     # complex number
print(type(x))  # Output: <class 'int'>
print(type(y))  # Output: <class 'float'>
print(type(z))  # Output: <class 'complex'>

# Setting the Data Type
x = int(3)     # x will be 3 - Integer
y = float(3)   # y will be 3.0 - Float
z = str(3)     # z will be '3' - String

x = "Hello World"
print(type(x))  # Output: <class 'str'> 

x= 20
print(type(x))  # Output: <class 'int'>

x = 20.5
print(type(x))  # Output: <class 'float'>

x = 1j
print(type(x))  # Output: <class 'complex'>

x = ["apple", "banana", "orange"]
print(type(x))  # Output: <class 'list'>

x = ("apple", "banana", "orange")
print(type(x))  # Output: <class 'tuple'>

x = range (6)
print(type(x))  # Output: <class 'range'>

x = {"name" : "James", "age" : "23"}
print(type(x))  # Output: <class 'dict'>

x = frozenset({"apple", "banana", "cherry"})
print (type(x))  # Output: <class 'frozenset'>

x = True
print(type(x))  # Output: <class 'bool'>

x = b"Hello"
print(type(x))  # Output: <class 'bytes'>

x = bytearray(5)
print(type(x))  # Output: <class 'bytearray'>

x = memoryview(bytes(5))
print(type(x))  # Output: <class 'memoryview'>

x = None
print(type(x))  # Output: <class 'NoneType'>