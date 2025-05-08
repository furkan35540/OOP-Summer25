#Creating Variables
x = 5
y = "Furkan"
print(x)
print(y)

x = 4
y = "Sally"
print(x)

#Casting
x = str(3)
y = int(3)
z = float(3)
print(y)
print(z)
print(z)

#Get the Type
x = 5
y = "Furkan"
print(type(x))
print(type(y))

#Single or Double
x = "Furkan"
print(x)
x = "Furkan"
print(x)

#Case-Sensitive
a = 4
A = "Furkan"

#Variable Name (Legal)
myvar = "Furkan"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
#illegal
2myvar = "John"
my-var = "John"
my  var = "John"

#Camel Case
myVariableName = "Furkan"
#Pacal Case
MyVariableName = "Furkan"
#Snake Case
my_variable_name = "Furkan"

#Many Values to Multiple Variables
x, y, z = "Orange","Banana","Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpack a Collection
fruits = ["apple","banana","cherry"]
x , y, z =fruits
print(x)
print(y)
print(z)

#Output Variables
x = "Python"
print(x)

#Example
x = "Furkan"
y = "Pilge"
z = "awesome"
print(x, y, z)

#Example
x = "Furkan"
y = "Pilge"
z = "awesome"
print(x + y + z)

#Example
x = 5
y = 10
print(x + y)

#Example Error
x = 5
y = "Furkan"
Print(x + y)

#Example
x = 5
y = "Furkan"
print(x , y)

#Global Variables
x = "Pilge"
def myfunc():
    print("Furkan"+ x)

myfunc()

#Example
x = "awesome"

def myfunc():
    x = "Pilge"
    print("Furkan" + x)

myfunc()
print("Furkan" + x)

#The global Keyword
def myfunc():
    global x
    x = "Pilge"

myfunc()
print("Furkan" + x)

#Example
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Furkan" + x)
