"""
This file will help us to learn Python Data Types
"""

#string
x = "Hello World"
print("\nType of x(=Hello World):", type(x))

#integer
x = 10
print("\nType of x(=10):", type(x))

#float
x = 60.6
print("\nType of x(=60.6):", type(x))

#complex
x = 2+3j
print("\nType of x(=2+3j):", type(x))

#complex
x = 4+6j
print("\nType of x(=4+6j):", type(x))

#float
x = 10E-10
print("\nType of x(=10E-10):", type(x))

#list
x = ["snehal", "Karale", "Red Hat"]
print("\nType of x(=[]):", type(x))

#tuple
x = ("Snehal", "Karale", "REdhat")
print("\nType of x(=()):", type(x))

#range
x = range(10)
print("\nType of x(=range(10)):", type(x))

#dict
x = {"A": "Snehal", "B": "Karale"}
print("\nType of x(={\"A\": \"Snehal\", \"B\": \"Karale\"}):", type(x))

#set
x = {"a", "b"}
print("\nType of x(={\"a\", \"b\"}):", type(x))

#frozenset
x = frozenset({"a","b"})
print("\nType of x (=frozenset):", type(x))

#bool
x = True
print("\nType of x(=True):", type(x))

#bytes
x = b"Snehal"
print("\nType of x(=b\"Snehal\"):", type(x))

#bytearray
x = bytearray(4)
print("\nType of x(=bytearray(4)):", type(x))

#memoryview
x = memoryview(bytes(6))
print("\nType of x(=memoryview(bytes(6))):", type(x))

#NoneType
x = None
print("\nType of x(=None):", type(x))