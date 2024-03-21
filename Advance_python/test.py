

from mod import MyClass,outside_method

# Creating an instance of Myclass
obj = MyClass("Test Object")


# Accessing member variables and methods of MyClass

print(obj.name)
print(obj.count)
obj.increment_count()
print(obj.count)

# Calling the outside method
outside_method()


# Todo 6) Create another file 'test.py' and without executing the 'mod.py' get it executed using the
# 'test.py' file.


from mod import MyClass,outside_method


#Todo  7)In 'test.py' create an object of the class defined in the 'mod.py'. Call the methods using the object. Make sure
# only that class is accessible and not the individual method to execute.


obj = MyClass(" Instance of MyClass")   # creating an object of MyClass
print("Name:", obj.name)    # Accessing member variables and calling methods


#Todo 8) The Method access from the file 'mod.py' is accessible in 'test.py'.

# Trying to access the outside_method - This will result in an AttributeError
try:
    outside_method()
except AttributeError:
    print("outside_method is not accessible from test.py")

print(obj.increment_count())       # 7) the class is accessible by method

print(outside_method())         # 8) calling a outside_method

from my_package.add import MyClass

obj=MyClass("anjum")
print(obj.get_name())       # 11) Use the object method of get & sum is access
print(obj.sum(10,20))


