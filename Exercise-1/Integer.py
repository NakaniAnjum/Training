

# Todo 1. Create a Integer Variable and convert it to Float, Boolean, String

# x=int(input("Enter any Integer::"))
# y=float(x)
# print(y)
# print(type(y))

# y=bool(x)
# print(y)
# print(type(y))

# y=str(x)
# print(y)
# print(type(y))


# Todo 2. Create a Float Variable and convert it to Integer, Boolean and String.

# x=float(input("Enter any float number::"))
# y=int(x)
# print(type(y))
# print(y)
#
# x=float(input("Enter any float number::"))
# y=bool(x)
# print(type(y))
# print(y)
#
# x=float(input("Enter any float number::"))
# y=str(x)
# print(type(y))
# print(y)

# Todo 3. Create a Boolean Variable and convert it to Integer, Float and String.


# x=bool(input("Enter any boolean value ::"))
# y=int(x)
# print(type(y))
# print(y)

# y=float(x)
# print(type(y))
# print(y)

# y=str(x)
# print(type(y))
# print(y)



# Todo 4. Create a String Variable and convert it to Integer, Float and Boolean

# x="21"
# y=int(x)
# print(type(y))
# print(y)
#
# x="22.19"
# y=float(x)
# print(type(y))
# print(y)
#
# y=bool(x)
# print(type(y))
# print(y)

# Todo 5. Find out values in String, Integer and Float when converting to Boolean it gives False

# a=""
# b="  "
# c=0
# d=0.0

# print(bool(a))
# print(bool(b))
# print(bool(c))
# print(bool(d))


# Todo 6.Perform operations with all the Arithmetic Operators

# a=int(input("Enter first number::"))
# b=int(input("Enter second number::"))

# c= a+b     # ADDITION
# print(c)

# c= a-b      # SUBTRACTION
# print(c)

# c= a*b      #MULTIPLICATION
# print(c)

# c= a%b      #MODULUS
# print(c)

# c= a/b      #DIVISION
# print(c)

# Todo 7. Perform operations with all the Bitwise Operators

# a=0b1010
# b=0b1100
#
# c= a&b              # BITWISE AND
# print(bin(c))
#
# c=a|b               # OR
# print(bin(c))
#
# c=a^b               #XOR
# print(bin(c))
#
# c= ~a                #NOT
# print(bin(c))
#
# c=a>>b              #Right shift
# print(bin(c))
#
# c=a<<b              #Left shift
# print(bin(c))

# Todo 8. Perform operations with all the Relational Operators

# x=4
# y=6

# c=x<y               #Greater than
# print(c)

# c =x>y              #less than
# print(c)

# c=x<=y              #less than equal to
# print(c)

# c=x>=y              #Greater than equal to
# print(c)

# c=x==y              #Equal to
# print(c)

# c=x!=y              #Not Equal to
# print(c)


# Todo 9. Perform operations with all the Logical Operators

# a=10            # AND operator
# b=20
# c=30
#
# if a>b and b>c:
#     print("a is the largest number ::")
#
# else:
#     print("a is not the largest number ::")
#

# Todo OR operator

# a=30
# b=50
# c=10
#
# if a>b or a>c:
#     print("a is the largest number ::")
#
# else:
#     print("a is the smallest number ::")
#

 #Todo Logical NOT operator

# a=10
# b=20
# c=30
#
# if not(a > b or a > c):
#     print("a is not the Largest number ::")
#
# else:
#     print("a is not the smallest number ::")
#

# Todo 10. Create a python script/program that will take input from the user for 3 numbers
# and result will print the biggest number and the smallest number using 'input' and  'print'.
#
# a=int(input("Enter first number::"))
# b=int(input("Enter second number::"))
# c=int(input("Enter Third number::"))
#
# if a>b and a>c:
#     print("a is the largest number ::")
#
# elif b>a and b>c:
#     print("b is the largest number ::")
#
# else:
#     print("c is the largest number ::")



#  Todo 11. Create another script/program using 'input' and pass all the three parameters as a
# single input and execute the same program as mentioned above.


# a,b,c=input("Enter three numbers::").split()

# if a>b and a>c:
#     print("a is the largest number ::")

# elif b>a and b>c:
#     print("b is the largest number ::")

# else:
#     print("c is the largest number ::")


# Todo 12. Print odd numbers between 1 to 10 in reverse order using while.

# i=10
# while(i>=1):
#     if(i%2!=0):
#         print(i, end=" ")
#     i-=1


# Todo 13. Perform the same operation with for loop.
#
# for i in range(10,0,-1):
#     if (i%2!= 0):
#          print(i)

# Todo 14. Print odd numbers between 1 to 10 using continue in both for and while loop.

# for num in range(1,11):   # USING FOR LOOP
#     if (num %2==0):
#         continue
#     print(num)

# num=1                     #USING WHILE LOOP
# while (num<=10):
#     if (num % 2==0):
#         num+=1
#         continue
#     print(num)
#     num+=1

# Todo 15.Take 10 numbers in a list(array) and print only first 3 numbers using loop.

# num=[1,2,3,4,5,6,7,8,9,10]
#
# for i in range (3):
#     print(num[i])

# Todo 16. Create a function which will not take any argument but will print numbers from 1 to 10.

# def my_fun():
#     for num in range(1,11):
#         print(num)
#
# my_fun()

# Todo 17. Create a function which will take 4 arguments where 2 will be mandatory and 2 keyword arguments. Perform multilpication if 2 values are passed.
# Perform addition if 3 are passed. Perform addition of 1st two operands and 2nd two operands and then do a subtraction if 4 arguments are passed.

# def my_fun (a,b, c=None, d=None):
#     if c is None and d is None:
#         return a * b
#
#     elif c is not None and d is None:
#                return a + b + c
#
#     elif c is not None and d is not None:
#         return (a + b) - (c + d)
#
#     else:
#         return "Invalid input"
#
# result1 = my_fun(2, 3)
# print(result1)
#
# result2 = my_fun(2,3,4,5)
# print(result2)
#
# result3 = my_fun(2, 3, c=4, d=1)
# print(result3)


# Todo 18. Create a function that will take unlimited arguments and should add all the arguments which are passed.

# def fun(*args):
#     return sum(args)
#
# argu1 = fun(1, 2, 3, 4, 5)
# print(argu1)
#
# argu2 = fun(10, 33, 1, 30)
# print(argu2)
#
#
#  # USING LAMBDA FUNCTION()
#
# arguments = lambda *args: sum(args)
# print(arguments(4, 4, 2, 1))  # output: 11
#
#
# # USING SUM FUNCTION()

# def arguments(*args):
#     return sum(args)
#
# print(arguments(5, 5, 5, 5))  # output: 20
#


# Todo 19. Create a function which will take unlimited arguments both non keyword and  keyword arguments. Add the values of all non
# keyword arguments and also the value of keyword arguments.

# def arguments(*args, **kwargs):
#     return sum(args) + sum(kwargs.values())
#
# print(arguments(1, 5,8,9,10, a=4, b=5,c=20,d=345))  # Output: 407
#


# Todo 20.Write a function with recursion to give the power of a number. It will be having two parameters no and power.If no power is passed
#  it should take 0.

# def num(no, power=0):
#     if power == 0:
#         return 1
#
#     elif power > 0:
#         return no * num(no,power -1)
#
#     else:
#         return 1 / num(no, -power)
#
# print(num(4, 3))        # output: 8
# print(num(3))                     # output: 1
# print(num(4, -2))



# Todo 21. Create a function with recursion which will find the factorial of a given no.
# def fact(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * fact(n - 1)
#
# result = fact(4)
# print(result)

#Todo 22. Create a script/program that will take arguments as 1,2,3,4,5, or 6 and will also take operands as arguments based on the selection made
 # it will perform the # operation and print the result.• 1=Addition, 2=Subtraction, 3=Multiplication, 4=Division, 5=Exponent,6=Floor Division. If anything else is passed it should say Invalid argument.
 # Create a parent function which will accept the options and based on the options it will call nested functions for each operation. So total 7 functions
 # will be# created one parent and 6 nested functions. • According to the selection made take inputs for the operations. If 1,2,3 are selected take 3 inputs as operands and if 4,5,6 are selected take 2 inputs as operands.
 # Perform the operation and print the result.

# def operation(option):
#     def add(a, b, c):
#         return a + b + c
#
#     def sub(a, b, c):
#         return a - b - c
#
#     def multi(a, b, c):
#         return a * b * c
#
#     def div(a, b):
#         if b != 0:
#             return a / b
#         else:
#             return "division by zero"
#
#     def exponent(a, b):
#         return a ** b
#
#     def floor_div(a, b):
#         if b != 0:
#             return a // b
#         else:
#             return " Floor division by zero"
#
#     if option == 1 or option == 2 or option == 3:
#
#         a = float(input("Enter the first operand: "))
#         b = float(input("Enter the second operand: "))
#         c = float(input("Enter the third operand: "))

#     elif option == 4 or option == 5 or option == 6:
#
#         a = float(input("Enter the first operand: "))
#         b = float(input("Enter the second operand: "))

#     else:
#         print("Invalid argument")
#         return
#
#     if option == 1:
#         print("Result:", add(a, b, c))
#     elif option == 2:
#         print("Result:", sub(a, b, c))
#     elif option == 3:
#         print("Result:", multi(a, b, c))
#     elif option == 4:
#         print("Result:", div(a, b))
#     elif option == 5:
#         print("Result:", expo(a, b))
#     elif option == 6:
#         print("Result:", floor_div(a, b))
#
# select_option = int(input("Select an operation (1=Add, 2=Sub, 3=Multi, 4=Div, 5=Exp, 6=Floor Div): "))
# operation(select_option)


# Todo  23. Create a two funcitons. Call one function from another function
#
# def first():
#     return "Hello, "
#
# def second():
#     merge= first()
#     return merge + " Good Morning !"
#
# print(second())


# Todo 24. Create a function that will take 5 arguments 2 will be mandatory and 3 will be keyword parameters. If 2 parameters are passed perform
#  multiplication of 2 parameters. If 3 parameters are passed print all the 3 parameters. If 4 parameters are passed addition of 4 parameters.
#  If 5 parameters are passed multiply 2 mandatory parameters and then separately multiply 3 keyword parameters and add both of them.


# def my_fun(param1, param2, *, param3=None, param4=None, param5=None):
#     if param3 is None and param4 is None and param5 is None:
#         # Only 2 parameters are passed
#         result = param1 * param2
#         print("Multipli of 2 para:", result)
#
#     elif param4 is None and param5 is None:
#         # 3 parameters are passed
#       print("parameters:", param1, param2, param3)
#
#     elif param5 is None:
#         # 4 parameters are passed
#         result = param1 + param2 + param3 + param4
#         print("Addi of 4 para:", result)
#
#     else:
#         # 5 parameters are passed
#         result = param1 * param2
#         keyword_result = param3 * param4 * param5
#         final_result = result + keyword_result
#         print("Multi of 2 mandatory parameters:", result)
#         print("Multi of 3 keyword parameters:", keyword_result)
#         print("sum of both):", final_result)
#
# my_fun(1, 2)
# my_fun(2, 2, param3=1)
# my_fun(2, 3, param3=1, param4=9)
# my_fun(2, 7, param3=4, param4=4, param5=7)

# Todo 25. Define a class and define two member variables and two methods inside the class.  One method will have one parameter
#  and other method will not have any parameter. Create a constructor for the class accepting two parameters and assign them to the class
#  member variables. One of the two methods will perform an operation on the member variables and give result. The second method will print
#  the result.

class myclass:
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2

    def method1(self, param):               # Method with parameter
        return self.var1 + self.var2 + param

    def method2(self):
        result = self.var1 * self.var2      #Method without parameter
        print("Result:", result)

obj = myclass(2, 6)
print(obj.method1(10))
obj.method2()



# Todo 26. Create a parent class and a child class. Create two methods in the parent class. Create one method in the child class. Create an
#  object of parent and try to access the method of parent and child class. Create an object of child class and try to access the method of parent
#  and child class.

# class parent:
#     def parent_method1(self):
#         print("This is first parent method ")
#     def parent_method2(self):
#         print("This is second parent method ")
#
# class child(parent):
#     def child_method(self):
#         print("This is child first method")
#
# parent_obj = parent()
#
# # Accessing methods of the parent class
# parent_obj.parent_method1()
# parent_obj.parent_method2()
#
# # Trying to access method of child class using object of parent class (not possible)
# # parent_obj.child_method()  # This line would raise an AttributeError
#
# # Creating an object of the child class
# child_obj = child()
#
# # Accessing methods of the parent class using object of child class
# child_obj.parent_method1()
# child_obj.parent_method2()
#
# child_obj.child_method()

# 27.Create a constructor and destructor for the above class.

# class parent:
#     def __init__(self):
#         print("Parent constructor")
#
#     def __del__(self):
#         print("Parent destructor")
#
#     def parent_method1(self):
#         print("This is parent first method")
#
#     def parent_method2(self):
#         print("This is parent second method")
#
# class child(parent):
#     def __init__(self):
#         super().__init__()
#         print("Child constructor")
#
#     def __del__(self):
#         print("Child destructor")
#         super().__del__()
#
#     def child_method(self):
#         print("This is child method")
#
# parent_obj =parent()
# print("parent obj is called")
#
# child_obj = child()
# print("child obj is called")
#
# # Accessing methods of the parent class using object of child class
# child_obj.parent_method1()
# child_obj.parent_method2()
# print("")
#
# # Accessing method of child class
# child_obj.child_method()
# print(" ")
#
# del parent_obj
# del child_obj

# 28. Override and Overwrite a method of the parent class in child class.

# class parent:
#     def parent_method(self):
#         print("This is the parent class method")
#
#
# class child(parent):
#     def parent_method(self):  # Overriding parent class method
#         print("This is the child class method")
#
#     def new_method(self):  # Overwriting parent class method
#         print("This is a new method in the child class")
#
#
# # Creating an object of the child class
# child_obj = child()
#
# # Overridden method from parent class
# child_obj.parent_method()
#
# # Overwritten method in child class
# child_obj.new_method()


# 29. Implement multiple inheritance and multi-level inheritance.

# Multiple Inheritance
# class parent1:
#     def method1(self):
#         print("method of parentClass1")
# class parent2:
#     def method2(self):
#         print("method of parentClass2")
#
# class child(parent1, parent2):
#     def child_method(self):
#         print("child method")
#
# child_obj = child()
#
# # Accessing methods from both parent classes
# child_obj.method1()
# child_obj.method2()
# print("")
#
# # Multi-level Inheritance
# class grandparents:
#     def grandparents_method(self):
#         print("grandparents method")
#
# class parent(grandparents):
#     def parent_method(self):
#         print("parent method")
#
# class grandchild(parent):
#     def grandchild_method(self):
#         print("grandchild Method")
#
# grandchild_obj = grandchild()
#
# grandchild_obj.grandparents_method()
# grandchild_obj.parent_method()
# grandchild_obj.grandchild_method()


''' 30. Perform overloading for constructors and methods defined in the class.'''

# class myclass:
#     def __init__(self, param1=None, param2=None):
#
#         if param1 is not None and param2 is not None:
#              self.param1 = param1           # Constructor with two parameters
#              self.param2 = param2
#
#         elif param1 is not None:
#             self.param1 = param1         # Constructor with one parameter
#             self.param2 = None
#
#         else:                            # Default constructor
#             self.param1 = None
#             self.param2 = None
#
#     def my_method(self, param1=None, param2=None):
#
#         if param1 is not None and param2 is not None:           # Method with two parameters
#             return param1 + param2
#
#         elif param1 is not None:                                # Method with one parameter
#             return param1
#
#         else:
#             return "no parameter"
#
# obj1 = myclass()
# print(obj1.my_method())
#
# obj2 = myclass(10)
# print(obj2.my_method())
#
# obj3 = myclass(10, 20)
# print(obj3.my_method())


'''31. Define a class(my_parent_class) with 2 variables x,y and 3 methods. add, sub and print_result. Define a child class and override the
methods and constructor as given below.

=> Parent Class:
• The methods add,sub will have two params which will be 2 default parameters
and print_result will not have any params.'''

# Create a constructor for this class with 2 default parameters, if the values are
# passed in the object assign those values to the new 2 member variables(a,b)
# else assign the values which are already there in the existing member
# variables(x,y) to new 2 member variables(a,b).
# • Define the methods add and sub which will perform the operation of addition
# and subtraction respectively store the values in two new member variables
# (res1,res2) and call the method print_result. The print_result method will print
# these two member variables(res1,res2).
# • Create three objects, one with no values passed, one with single value passed
# and one with two value passed.
#
# => Child Class:
#
# • Inherit the parent class(my_parent_class) in a child class(my_child_class) and
# override the constructor to have an additional parameter which will be again a
# default parameter assigning the value to the child member variable(z).
# • Override add() method which will call the parent class add method using two
# variable but the print_result() method should print the addition of the 3
# member variables(x,y,z) instead of two(x,y) without inheriting the
# print_result() method.
# • Override the sub() method to perform multiplication operation of three member
# variables(x,y,z) instead of subtraction of two member variables(x,y)
# • Override a destructor to show when it is being called automatically and when it
# would be called manually by our code.

# class my_parent_class:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def add(self, a=0, b=0):
#         self.res1 = self.x + a
#         self.res2 = self.y + b
#         self.print_result()
#
#     def sub(self, a=0, b=0):
#         self.res1 = self.x - a
#         self.res2 = self.y - b
#         self.print_result()
#
#     def print_result(self):
#         print(f"Result 1: {self.res1}")
#         print(f"Result 2: {self.res2}")
#
#
# class my_child_class(my_parent_class):
#     def __init__(self, x=0, y=0, z=0):
#         super().__init__(x, y)
#         self.z = z
#
#     def add(self, a=0, b=0):
#         super().add(a, b)
#         result3 = self.x + self.y + self.z
#         print(f"Result 3: {result3}")
#
#     def sub(self, a=0, b=0):
#         result3 = self.x * self.y * self.z
#         print(f"Multiplication of x, y, and z: {result3}")
#
#     def _del_(self):
#         print("Destructor called")
#
#
# # Creating parent class objects
# obj1 = my_parent_class()
# obj2 = my_parent_class(5)
# obj3 = my_parent_class(3, 7)
#
# # Creating child class object
# child_obj = my_child_class(2, 4, 6)
#
# # Testing the parent class objects
# obj1.add()
# obj2.sub(2, 1)
# obj3.add(4, 3)
#
# # Testing the child class object
# child_obj.add(1, 2)
# child_obj.sub()

