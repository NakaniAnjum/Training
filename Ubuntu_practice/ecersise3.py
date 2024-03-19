## todo 1. Generate At least 5 different Errors.


 #  # SyntaxError: '(' was never closed
#print("Hello, World!"


 # # IndentationError: expected an indented block after function definition on line 4
# def my_function():
# print("Indented statement")

#  Name ERROR name 'x' is not defined
# print(x)

# TypeError: can only concatenate str (not "int") to str
# x = 'hello'
# y = 10
# z = x + y
# print(z)

#  FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent_file.txt'
#file = open("nonexistent_file.txt", "r")


# todo 2. Handle all the 5 different Erros using Exception Handling.
# try:
#     a = int(input('enter number'))
#     l = [6,3]
#     print(l[a])
#     x = 'hello'
#     y = 10
#     z = x + y
#     print(z)
#     print(b)
#     file = open("nonexistent_file.txt", "r")
# except ValueError as e:
#     print(e)
# except IndexError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# except NameError as e:
#     print(e)
# except FileNotFoundError as e:
#     print(e)


# todo 3. Handle an error with try-except-else.


# try:
    # a = int(input('enter number'))
    # l = [6,3]
    # print(l[a])
    # x = 'hello'
    # y = 10
    # z = x + y
    # print(z)
    # b= 5
    # print(b)
    # file = open("nonexistent_file.txt", "r")
# except ValueError as e:
#     print(e)
# except IndexError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# except NameError as e:
#     print(e)
# except FileNotFoundError as e:
#     print(e)
# except:
#     print('invalid ')
# else:
#     print("this is else part of the file") # no error than else part are executed




# todo 4. Handle an error with try-except-else-finally.
# try:
    # a = int(input('enter number'))
    # l = [6,3]
    # print(l[a])
    # x = 'hello'
    # y = 10
    # z = x + y
    # print(z)
    # b = 5
    # print(b)
    # file = open("nonexistent_file.txt", "r")
# except ValueError as e:
#     print(e)
# except IndexError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# except NameError as e:
#     print(e)
# except FileNotFoundError as e:
#     print(e)
# except:
#     print('invalid ')
# else:
#     print("this is else part of the file") # no error than else part are executed

# finally:
#     print("this code always are excuted")

 # todo 5. Use raise for generating User Defined Exception for minimum length of a list should be 5.

# a = int(input('enter a number '))
# l=[10,20,3,0,4,5,6,7,8,9]
# if (len(l) <= a):
#     raise ValueError("not a valid amount")


 # todo 12.Create a script/program to open a file to write a string. Write a string in a file 'test_file.txt'.

# f = open("test_file.txt",'w')
#
# f_str='''this is a content of text file.
# it manage the file management concept.
#  this is a string to store in the file.
#  this is the file management string .
#  this is the last line of the file.'''
#
# f.write(f_str)
# f.close()

# todo 13.Create a script/program to open a file 'test_file.txt' to read a string. Read the whole string content from the file and print it.
# f = open("test_file.txt",'r+')
# f_str=f.read()
# print(f_str)

# todo 14.Create a script/program to open a file 'test_file.txt' to read the content line by line and print it.
# f3 = f.readline() # read first line of the file
# print(f3)
#
# f2 =f.read()
# print(f2)
# #
# f4 = f.readlines() # convert string into list
# print(f4)


# todo 15.Create a script/program to open a file 'test_file.txt' to append a string at the end of the existing string in a file.
# f = open("test_file.txt",'a')
#
# f_str=''' this is add content of the file .
# this is new content of the file.'''
#
# f5 = f.write(f_str)
# print(f5)


# todo 16.Create a script/program to write and read binary data in a file 'test_file.data'.

# # Writing binary data
# with open("test_file.data", "wb") as file:
#     data_to_write = b"Hello, binary world!"  # Sample binary data
#     file.write(data_to_write)
#
# # Reading binary data
# with open("test_file.data", "rb") as file:
#     data_read = file.read()
#     print("Read binary data:", data_read)


# todo 17. Using pickle dump no of variables with different data types in a file 'my_variables.data'.

# import pickle

# my_int = 42
# my_float = 3.14
# my_string = "Hello, world!"
# my_list = [1, 2, 3, "four"]
# my_dict = {"name": "Bard", "age": 3}

# with open("my_variables.data", "wb") as file:
#     pickle.dump(my_int, file)
#     pickle.dump(my_float, file)
#     pickle.dump(my_string, file)
#     pickle.dump(my_list, file)
#     pickle.dump(my_dict, file)
#
# print("Variables pickled successfully!")

# import pickle
# f =open("sample.txt",'rb')
# l=pickle.load(f) # read the data that will be store in file
# print(l)

# todo 18.Create another script/program and read the dumped variables in the file 'my_variables.data'.
# import pickle
#
# with open("my_variables.data", "rb") as file:
#     my_int = pickle.load(file)
#     my_float = pickle.load(file)
#     my_string = pickle.load(file)
#     my_list = pickle.load(file)
#     my_dict = pickle.load(file)
#
# print("Integer:", my_int)
# print("Float:", my_float)
# print("String:", my_string)
# print("List:", my_list)
# print("Dictionary:", my_dict)


# import pickle
#
# l =[10,20,30,40,50] # store data in binary format
# file =open("test_file.txt",'wb')
# pickle.dump(l,file)
# file.close()

# todo 19.Print the current date using datetime and date libraries.
#
# import datetime
# crt_dt_tm = datetime.datetime.now()
# print(crt_dt_tm)

# todo 20.Convert a datetime to a string.

# current_date = datetime.date.today()
# # Format the date
# formatted_date = current_date.strftime("%Y/%m/%d")
# print("Formatted Date:", formatted_date)

# todo 21.Get the difference between two dates in days.

# from datetime import datetime
# date1 = datetime(2024, 2, 6)
# date2 = datetime(2024, 1, 15)
# difference = date1 - date2
# difference_in_days = difference.days
# print("difference :", difference_in_days)

# todo 22.Calculate your age in years, months and days.

# from datetime import datetime
# birthdate = datetime(2001, 12, 2)  # Example birthdate
# current_date = datetime.now()
# difference = current_date - birthdate
# years = difference.days // 365
# months = (difference.days % 365) // 30
# days = (difference.days % 365) % 30
#
# print("Your age is:", years, "years,", months, "months, and", days, "days.")


# todo 23.Get the date which is 1 week from today's date.

# from datetime import datetime, timedelta
# today = datetime.now()
# one_week_from_today = today + timedelta(days=7)
#
# print("one week from today's date:", one_week_from_today.strftime("%Y-%m-%d"))


# todo 24.Get the date which is 1 year from today's date.

# from datetime import datetime
# from dateutil.relativedelta import relativedelta
# today = datetime.now()
# one_year_from_today = today + relativedelta(years=1)
# print("one year from today's date:", one_year_from_today.strftime("%Y-%m-%d"))

# todo from datetime import datetime
# from dateutil.relativedelta import relativedelta
#
# # Get today's date
# today = datetime.now()
#
# # Calculate the date which is 1 year from today
# one_year_from_today = today + relativedelta(years=1)
#
# print("One year from today's date:", one_year_from_today.strftime("%Y-%m-%d"))

# todo 25.Get the date which is 1 month from today's date.

# from datetime import datetime
# from dateutil.relativedelta import relativedelta
# today = datetime.now()
# one_month_from_today = today + relativedelta(months=1)
#
# print("One month from today's date:", one_month_from_today.strftime("%Y-%m-%d"))

# todo 26.Get the 1st day of the current month from today's date.

# from datetime import datetime
# today = datetime.now()
# first_day_of_current_month = today.replace(day=1)
#
# print("1st day of the current month:", first_day_of_current_month.strftime("%Y-%m-%d"))

# todo 27.Get the 1st month of the current year from today's date.

# from datetime import datetime
# today = datetime.now()
# first_month_of_current_year = today.replace(month=1, day=1)
#
# print("1st month of the current year:", first_month_of_current_year.strftime("%Y-%m-%d"))

# todo 28.Get the dates of current month starting from Monday to Sunday in a list.

# from datetime import datetime, timedelta
# today = datetime.now()
# first_day_of_month = today.replace(day=1)
# first_monday = first_day_of_month + timedelta(days=(0 - first_day_of_month.weekday()))
# dates_of_current_month = []
#
# current_date = first_monday
# for _ in range(7):
#     dates_of_current_month.append(current_date)
#     current_date += timedelta(days=1)
#
# # Print the dates
# for date in dates_of_current_month:
#     print(date.strftime("%Y-%m-%d"))




# todo 29. Get the first date and last date of the current month.
# from datetime import datetime, timedelta
# today = datetime.today()
# first_date_of_month = today.replace(day=1)
# last_date_of_month = today.replace(day=1, month=today.month+1) - timedelta(days=1)
#
# print("First date of the current month:", first_date_of_month.strftime("%Y-%m-%d"))
# print("Last date of the current month:", last_date_of_month.strftime("%Y-%m-%d"))


# todo 30.Get me the 1st and last date of the current month in the format as following. '14th June 2016 Tuesday 10:00:00 AM'
# from datetime import datetime, timedelta
# today = datetime.today()
# first_date_of_month = today.replace(day=1)
# last_date_of_month = today.replace(day=1, month=today.month+1) - timedelta(days=1)
#
# # Define a function to convert day number to ordinal (e.g., 1st, 2nd, 3rd, etc.)
# def ordinal(n):
#     if 10 <= n % 100 <= 20:
#         suffix = 'th'
#     else:
#         suffix = {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
#     return str(n) + suffix
#
# # Format the dates in the desired format
# formatted_first_date = first_date_of_month.strftime("%dth %B %Y %A %I:%M:%S %p")
# formatted_last_date = last_date_of_month.strftime("%dth %B %Y %A %I:%M:%S %p")
#
# # Print the formatted dates
# print("First date of the current month:", formatted_first_date)
# print("Last date of the current month:", formatted_last_date)
#
#
# # todo 31.Get me random number from 1 to 100.
#
# import random
# print(random.randrange(1,100))

# todo 32.Get me a random combination of 4 different numbers between 1 to 100.
# import random
# random_numbers = random.sample(range(1, 101), 4)
# print(random_numbers)


# todo 33.You have a sorted list from 1 to 10 you have to unsort it.
#
# import random
# sorted_list = list(range(1, 11))
# random.shuffle(sorted_list)
# print("unsorted list:", sorted_list)

# todo 34.Execute a shell script command from python code

# import os
# os.system("ls -l")
# os.mkdir("data")
# print(os.getcwd())



# todo 35.Create a regular expression to check a valid URL.

# import re
# url_pattern = re.compile(r"^(http|https):\/\/([\w-]+\.)+[\w-]+(\/[\w\- ./?%&=]*)?$")
# urls = [
#     "http://www.example.com",
#     "https://skyscendbs.com/",
#     "https://www.example.com/path/to/page?query=example",
#     "ftp://ftp.example.com",  # Not a valid URL
#     "http://invalid domain.com",  # Not a valid URL
# ]
#
# # Check if each URL is valid
# for url in urls:
#     if url_pattern.match(url):
#         print(f"{url} is a valid URL.")
#     else:
#         print(f"{url} is not a valid URL.")

# todo 36. Create a regular expression to check a valid email.

# import re
# email_pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
# emails = [
#     "example@example.com",
#     "dafdaanjana75@gmail.com",
#     "12208101.gvp@gujaratvidyapith.org",
#     "anjanadafda.skyscendbs@gmail.com",
#     "invalid.email@com",
#     "invalid@email",
# ]
# for email in emails:
#     if email_pattern.match(email):
#         print(f"{email} is a valid email address.")
#     else:
#         print(f"{email} is not a valid email address.")


# todo 37. Create a regular expression to check a valid Pin code of India.

# import re
# pin_pattern = re.compile(r"^[1-9][0-9]{5}$")
# pincodes = [
#     "110001",
#     "400705",
#     "123456",
#     "98765",
#     "ABCDE",
# ]
# for pincode in pincodes:
#     if pin_pattern.match(pincode):
#         print(f"{pincode} is a valid Indian PIN code.")
#     else:
#         print(f"{pincode} is not a valid Indian PIN code.")

# todo 38. Create a class Student and add member variables with False values. The variables
#  are as listed below. Marks will have a default value blank list.
#  1. Name
#  2. Reg No
#  3. Roll No
#  4. Standard
#  5. Admission Year
#  6. Marks
#  7. Result
#  Add a constructor that will assign Name, Reg No, Roll No, Standard, Admission
#  year. In the constructor add validation for Name to be only Alphabetic, Reg No to be
#  alphanumeric, Roll No, Standard nad Admission year to be numeric. All above
#  values will be accepted as string only. If the passed parameters are not string raise
#  and Error to the user.
#  Add a method that will accept a dictionary for marks containing subject as key and
#  marks as values. It will add the dictionary to the list of marks. Marks list will have
#  multiple elements and each element will be a dictionary only. Here there should be a
#  validation to accept the marks which are less than or equal to 100 only. If the
#  obtained marks are less than 40 the result will be fail otherwise pass. In the
#  dictionary the result can be added.
#  Add another method that will generate the result. This method will check if there
#  is any line in the marks having fail as result the result will be Fail and it will print the
#  complete result as following.
#  If any of the result is Fail the Percentage will not be shown and only -- will be
#  printed instead.
#  Define a function to calculate the grade. For Example if the result is fail for any
#  subject it will be F grade. If the Percentage is 95+ it will be O+. If the percentage is
#  90+ and less than 95 then it will be O. If the percentage is 85+ and less than 90 it will
#  be A+. If the Percentage is 80+ and less than 85 it will be A. If the Percentage is 75+
#  and less than 80 it will be a B+. If the percentgae is 70+ and less than 75 it will be B.
#  If the Percentage is 60+ and less than 70 it will be C. If the percentage is 50+ and
#  less than 60 it will be D. If the percetage is 40+ and less than 50 it will be E. The
#  Grade must be displayed on the result which is shown below.




class Student:
    def __init__(self, name, reg_no, roll_no, standard, admission_year):
        self.validate_input(name, reg_no, roll_no, standard, admission_year)
        self.name = name
        self.reg_no = reg_no
        self.roll_no = roll_no
        self.standard = standard
        self.admission_year = admission_year
        self.marks = []
        self.result = False
        self.total_marks = 0  # Total marks obtained

    def validate_input(self, name, reg_no, roll_no, standard, admission_year):
        if not all(isinstance(value, str) for value in [name, reg_no, roll_no, standard, admission_year]):
            raise ValueError("Name, Reg No, Roll No, Standard, and Admission Year must be strings.")

        if not name.isalpha():
            raise ValueError("Name must contain only alphabetic characters.")

        if not reg_no.isalnum():
            raise ValueError("Reg No must be alphanumeric.")

        if not all(value.isdigit() for value in [roll_no, standard, admission_year]):
            raise ValueError("Roll No, Standard, and Admission Year must be numeric.")

    def add_marks(self, marks_dict):
        for subject, mark in marks_dict.items():
            if not isinstance(mark, int) or mark < 0 or mark > 100:
                raise ValueError("Marks must be integers between 0 and 100.")
            self.marks.append({subject: mark})
            if mark < 40:
                self.result = "Fail"
            self.total_marks += mark  # Increment total marks

    def generate_result(self):
        if self.result == "Fail":
            print("Result: Fail")
            print("--")
        else:
            percentage = self.total_marks / (len(self.marks) * 100) * 100
            grade = self.calculate_grade(percentage)
            print("Result: Pass")
            print("Total Marks:", self.total_marks)
            print("Percentage:", percentage)
            print("Grade:", grade)

    def calculate_grade(self, percentage):
        if percentage >= 95:
            return "O+"
        elif percentage >= 90:
            return "O"
        elif percentage >= 85:
            return "A+"
        elif percentage >= 80:
            return "A"
        elif percentage >= 75:
            return "B+"
        elif percentage >= 70:
            return "B"
        elif percentage >= 60:
            return "C"
        elif percentage >= 50:
            return "D"
        elif percentage >= 40:
            return "E"
        else:
            return "F"


# Get user input to create a student object
name = input("Enter student's name: ")
reg_no = input("Enter student's registration number: ")
roll_no = input("Enter student's roll number: ")
standard = input("Enter student's standard: ")
admission_year = input("Enter student's admission year: ")

# Create a student object
student = Student(name, reg_no, roll_no, standard, admission_year)

# Get user input for marks
num_subjects = int(input("Enter the number of subjects: "))
marks_dict = {}
for i in range(num_subjects):
    subject = input(f"Enter subject {i+1} name: ")
    mark = int(input(f"Enter marks for {subject}: "))
    marks_dict[subject] = mark

# Add marks to the student object
student.add_marks(marks_dict)

# Generate and print the result
student.generate_result()














# todo 39. Optimize the following code and make it in two lines.
# x = {'a':1, 'b':2} – No Change
# if 'c' in x:
# y = x['c']
# else:
# y=0
#
# x = {'a':1, 'b':2}
# y = x['c'] if 'c' in x else 0
# print(y)


# todo 40. Consider a variable which has string value “Skyscend Business Solutions Pvt.
# Ltd.” print the following in one line.
# ◦ SKY
# ◦ SKYSCEND
# ◦ Bus
# ◦ solutions
# s = "Skyscend Business Solutions Pvt. Ltd."
# print(f"{s[:3].upper()}\n{s[:8].upper()}\n{s[9:12]}\n{s[18:27].lower()}")

# todo 41. Create a function using 'lambda' for exponent of a given number. Take two
#   arguments one as the number and the other one as the exponent.

# exponentiate = lambda x, y: x ** y
# result = exponentiate(2, 3)
# print(result)

# todo 42. Create an assertion for a string to check the length of the string being minimum of 10 letters.
# string = "thisisastring"  # same as raise but with condition
# assert len(string) >= 10, "String length must be at least 10 characters"

# todo 43. Read a file 'python.txt' which is containing python code and execute the python code which is read from the file.

# with open('python.txt', 'r') as file:
#     python_code = file.read()
# exec(python_code)


# todo 44. Using range get me a list of 1 to 10 and from this list generate a list as
#  [13,15,17,19,21,23,25,27,29,31]. Code needs to be done in one line only.

# result = [x + 12 for x in range(1, 11)]
# print(result)

# todo 45. Using range get me a list of even numbers between 1 to 100. Code needs to be done in one line only.

# even_numbers = [x for x in range(2, 101, 2)]
# print(even_numbers)

# todo 46. Generate a list of exponents of first 25 integers. Code needs to be in one line only.

# exponents = [i**i for i in range(1, 26)]
# print(exponents)

# todo 47. Create a generator method to have the prime numbers using yield between 1 to 100.

# def generate_primes():
#     for num in range(2, 101):
#         if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
#             yield num
#
# # Usage example:
# prime_generator = generate_primes()
# for prime in prime_generator:
#     print(prime)


# todo 48. Create a generator method which gives random numbers between 1 to 100 and the
#  number not being repeated. Make sure it generates only 10 numbers.

# import random
#
# def generate_unique_random_numbers():
#     generated_numbers = set()
#     while len(generated_numbers) < 10:
#         num = random.randint(1, 100)
#         if num not in generated_numbers:
#             generated_numbers.add(num)
#             yield num
#
# # Usage example:
# random_generator = generate_unique_random_numbers()
# for number in random_generator:
#     print(number)


# todo 49. Convert a decimal number '15' to binary, hexadecimal, octal numbers.

# binary_num = bin(15) # 1111
# print("binary no ",binary_num)
#
# octal_num = oct(15) # 17
# print("octal num",octal_num)
#
# hexadecimal_num = hex(15) # f
# print("hexadecimal no ",hexadecimal_num)

# todo 50. Convert a Hexadecimal number '10' to binary, decimal and octal numbers.
# hex_num ='10'
#
# binary_num=bin(int(hex_num,16))
# print("binary number",binary_num) # 10000
#
# octal_num=oct(int(hex_num,16))
# print("octal number",octal_num) # 20
#
# decimal_num =int(hex_num,16)
# print("decimal number is ",decimal_num) # 16

# todo 51. Convert an Octal number '13' to binary, decimal and hexadecimal numbers

# octal_num='13'
#
# binary_num =bin(int(octal_num,8))# 1011
# print("binary number is ",binary_num)
#
# hexadecimal_num =hex(int(octal_num,8)) # b
# print("hexadecimal number is",hexadecimal_num)
#
# decimal_num =int(octal_num,8) # 11
# print("decimal is",decimal_num)

# todo 52. Convert Binary number '11010001111100111' to decimal, hexadecimal and octal numbers.
#
# binary_num ='11010001111100111'
#
# decimal_num =int(binary_num,2)
# print("decimal is",decimal_num)
#
# octal_num=oct(int(binary_num,2))
# print("octal number",octal_num)
#
# hexadecimal_num = hex(int(binary_num,2))
# print("hexadecimal is",hexadecimal_num)

# todo 53. Create a dictionary containing all the Capital Letters 'A-Z', Small Letters 'a-z', and
#  Digits '0-9' as keys and their ascii values as values using generators.

# ascii_dict={chr(i):ord(chr(i))for i in range (48,58)}
# print(ascii_dict)
# ascii_dict.update({chr(i):ord(chr(i)) for i in range (65,91)})
# print(ascii_dict)
# ascii_dict.update({chr(i):ord(chr(i)) for i in range (97,123)})
# print(ascii_dict)

# todo 54. Get an absolute value of any negative integer.

# number = -15
# abs_num = abs(number)
# print(abs_num)

# todo 55. Compare two numbers and get me the maximum number with a built-in function.

# num1 = 10
# num2 = 20
#
# max_num = max(num1, num2)
# print("maximum number:", max_num)


# todo 56. Create a class with member variables. Now perform the following.
# class Myclass:
#     def __init__(self,attr1,attr2):
#         self.attr1 = attr1
#         self.attr2 = attr2
# #  1. Check whether an attribute exists in the class or not.
#     def check_attribute(self,attr_name):
#         return hasattr(self,attr_name)
#
# #  2. Fetch the value of an attribute of a class.
#     def get_att_value(self,attr_name):
#         if hasattr(self,attr_name):
#             return getattr(self,attr_name)
#         else:
#             return None
#
#     #  3. Update the value of an attribute of a class.
#     def update_att_valu(self,attr_name,new_value):
#         if hasattr(self,attr_name):
#             setattr(self,attr_name,new_value)
#             print(f"update{attr_name} to {new_value}")
#         else:
#             print(f"attribute {attr_name} does not exist")
#
#     #  4. Delete the attribute of a class.
#     def delete_att_value(self,attr_name):
#         if hasattr(self,attr_name):
#             delattr(self,attr_name)
#             print(f"delete attribute {attr_name}")
#         else:
#             print(f"atribute {attr_name}does not exist")
#
#
# obj = Myclass(10, "Hello")
#
# print(obj.check_attribute("attr1"))
# print(obj.check_attribute("attr3"))
#
# print(obj.get_att_value("attr1"))
# print(obj.get_att_value("attr2"))
# print(obj.get_att_value("attr3"))
#
# obj.update_att_valu("attr1", 20)
# print(obj.attr1)
#
# obj.delete_att_value("attr2")
# print(obj.check_attribute("attr2"))


# todo 57. Generate a list of having 10 elements using random but the numbers shoud be
#  either 1 or 0. Check if all the elements are 1 print “ALL” and if any of the single
#  element is 1 print “ANY” and if all the elements are 0 print “NONE”.

# import random
# random_list = [random.choice([0, 1]) for _ in range(10)]
# if all(num == 1 for num in random_list):
#     print("ALL")
# elif any(num == 1 for num in random_list):
#     print("ANY")
# else:
#     print("NONE")
#
# print("Generated list:", random_list)

# todo 58. Get 10 random numbers in a list and get the maximum number from the list.

# import random
# random_numbers = [random.randint(1, 100) for _ in range(10)]
# max_number = max(random_numbers)
# print("random numbers:", random_numbers)
# print("max number:", max_number)

# todo 59. Get 10 random numbers in a list and get the minimum number from the list.

# import random
# random_numbers = [random.randint(1, 100) for _ in range(10)]
# min_number = min(random_numbers)
# print("random numbers:", random_numbers)
# print("max number:", min_number)

# todo 60. Get 10 random numbers from 1 to 100 in a list and create two separate lists from
#  it for odd and even numbers using filter.

# import random
# random_numbers = [random.randint(1, 100) for _ in range(10)]
# odd_numbers = list(filter(lambda x: x % 2 != 0, random_numbers))
# even_numbers = list(filter(lambda x: x % 2 == 0, random_numbers))
# print("original list  random numbers:", random_numbers)
# print("odd numbers:", odd_numbers)
# print("even numbers:", even_numbers)


# todo 61. Using map generate cubes of first 10 numbers.

# cubes = list(map(lambda x: x ** 3, range(1, 11)))
# print("cubes first 10 numbers:", cubes)

# todo 62. Using map generate a list from two lists by multiplying the elements in the two
#  lists on the identical indexes in both the lists.

# l1 = [1, 2, 3, 4, 5]
# l2 = [6, 7, 8, 9, 10]
# result = list(map(lambda x, y: x * y, l1, l2))
# print("resulting list:", result)

# todo 63. Generate 15 random numbers from 1 to 100 and get the total of all these numbers.

# import random
# random_numbers = [random.randint(1, 100) for _ in range(15)]
# sum_num =sum(random_numbers)
# print(random_numbers)
# print(sum_num)

# todo 64. Get a list of 10 random characters and then merge all the characters in a single string

# import random
# import string
# random_characters = [random.choice(string.ascii_letters) for _ in range(10)]
# merged_string = ''.join(random_characters)
# print("random charcters:", random_characters)
# print("merged string:", merged_string)

# todo 65. Create a class with few methods and in one of the method get all the global
#  attributes that can be used in that method and also the local attributes that can be
#  used in that method.

# class MyClass:
#     def __init__(self, attr1, attr2):
#         self.attr1 = attr1
#         self.attr2 = attr2
#
#     def method_with_attributes(self):
#         global_attrs = globals()
#         local_attrs = locals()
#
#         print("Global attributes:")
#         for name, value in global_attrs.items():
#             print(f"{name}: {value}")
#
#         print("\nLocal attributes:")
#         for name, value in local_attrs.items():
#             print(f"{name}: {value}")
#
# obj = MyClass(14, "anjana")
# obj.method_with_attributes()

# todo 66. Create two classes one as a parent and the other as a child. Make a validation
#  whether the child is a subclass of parent or not.

# class Parent:
#     pass
# class Child(Parent):
#     pass
#
# if issubclass(Child, Parent):
#     print("child is a subclass of Parent.")
# else:
#     print("child is not a subclass of Parent.")




# todo 67. Get two lists ['a','b','c','d','e'],[1,2,3,4,5] and generate a single dictionary
#  {'a':1,'b':2,'c':3,'d':4,'e':5} with the identical indexed items.

# list1 = ['a', 'b', 'c', 'd', 'e']
# list2 = [1, 2, 3, 4, 5]
# result_dict = dict(zip(list1, list2))
#
# print(result_dict)





# todo 68. Sort a list of random 25 numbers between 1 to 100 without using the sort method.

# import random
# random_numbers = [random.randint(1, 100) for _ in range(25)]
# def sort_function(numbers):
#     n = len(numbers)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if numbers[j] > numbers[j+1]:
#                 numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
#
# sort_function(random_numbers)
# print("Sorted list:", random_numbers)






# todo  69. Sort the following list with the second element of the inner list. [[4, ’a’], [9, ’x’],
#  [10, ’c’], [25,’z’], [32, ‘b’]].

# l =[[4, 'a'], [9, 'x'], [10, 'c'], [25,'z'], [32, 'b']]
# res = sorted(l,key = lambda  e : e[0])
# print(res)



# todo 70. Create a function for addition of two numbers. Create a validation that both of
#  them must be either float or integer using a built in method.

# def add_numbers(num1, num2):
#     if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
#         return num1 + num2
#     else:
#         raise TypeError("Both numbers must be either float or integer")
#
# try:
#     result = add_numbers(5, 7.5)
#     print("Result:", result)
# except TypeError as e:
#     print("Error:", e)
#
# try:
#     result = add_numbers(5, '7')
#     print("Result:", result)
# except TypeError as e:
#     print("Error:", e)


# todo 71. Create a function and a nested function inside this function. Assign variables
#  outsie both the functions, define two variables inside the first function. Make on of
#  the variables to be global. Define other two variable inside the nested function and
#  make one of them global. Now call the locals() and globals() function from
#  outside both the functions, inside first function and inside the nested function and
#  check what is available as local and global variables which can be accessed.


# def outer_function():
#     # Variables outside both functions
#     global_var_outside = "I am global outside"
#     var_outside = "I am outside"
#
#     def inner_function():
#         # Variables inside the nested function
#         nonlocal global_var_outside
#         global_var_outside = "I am global inside"
#         var_inside = "I am inside"
#
#         # Make a variable global inside the nested function
#         global global_var_inside_function
#         global_var_inside_function = "I am also global inside function"
#
#         # Print local and global variables inside the nested function
#         print("Local variables inside nested function:", locals())
#         print("Global variables inside nested function:", globals())
#
#     # Call the nested function
#     inner_function()
#
#     # Print local and global variables inside the outer function
#     print("\nLocal variables inside outer function:", locals())
#     print("Global variables inside outer function:", globals())
#
#
# # Variables outside the function
# global_var_outside_main = "I am global outside main"
#
# # Call the outer function
# outer_function()
#
# # Print local and global variables outside all functions
# print("\nLocal variables outside all functions:", locals())
# print("Global variables outside all functions:", globals())
