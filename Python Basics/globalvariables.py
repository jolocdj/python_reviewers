# Python - Global Variables
# Global variables are variables that are defined outside of a function and can be accessed from any function in the program.

x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()

# If you need to create a global variable, but are stuck in the middle of a function, you can use the global keyword.
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)

