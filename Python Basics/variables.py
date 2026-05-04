# Python Variables
# Variables are containers for storing data values.

# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.

x = 5
y = "Hello, World!"
print (x)
print (y)

x = "Alden Richards"
y = "Yaya Dub"

print (y)

#Casting - If you want to specify the data type of a variable, this can be done with casting.

x = str(3.5)    # x will be '3' - String
y = int(3)    # y will be 3 - Integer
z = float(3)  # z will be 3.0 - Floar / Decimal

print (x)
print (y)
print (z)

#Get the type - You can get the data type of a variable with the type() function.

x = 5
y = "Hello, World!"
z = 2.5

print (type(x))
print (type(y))
print (type(z))

#Single or Double Quotes - String variables can be declared either by using single or double quotes:

x = "John"
y = 'John'

print(x)
print(y)

#Case Sensitivity - Variable names are case-sensitive. This means that 'myVariable' and 'myvariable' are considered different variables.


myVariable = "Jolo is handssome!"
myvariable = "Jolo is cute!"

print (myvariable)
print (myVariable)