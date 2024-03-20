

#Todo 1. Generate Atleassalaryt 5 different Errors.

# #1) Todo  Type Error:
# x = "5"
# y = 2
# print(x + y)  # Attempting to concatenate a string and an integer

# #2) Todo Indentation Error:
#
# def my_function():
# print("Indented line")  # Missing indentation
#
# #3) Todo Name Error:
#
# print(x)  # Variable x is not defined

#4)Todo  Syntax Error:

# print("Hello, world!"  # Missing closing parenthesis
#

#5) Todo ZeroDivisionError:
#
# x = 10
# y = 0
# print(x / y)  # Division by zero


#Todo 2.  Handle all the 5 different Erros using Exception Handling.


#1)Todo  TodoSyntax Error:

# try:
#     print("Hello, world!"
# except SyntaxError as e:
#     print("Syntax Error:", e)
#
# #2)Todo Indentation Error:
#
# def my_function():
#     try:
#         print("Indented line")
#     except IndentationError as e:
#         print("Indentation Error:", e)
#
# #3) Todo Name Error:
#
# try:
#     print(x)  # Variable x is not defined
# except NameError as e:
#     print("Name Error:", e)
#
# #4) Todo Type Error:
#
# try:
#     x = "5"
#     y = 2
#     print(x + y)  # Attempting to concatenate a string and an integer
# except TypeError as e:
#     print("Type Error:", e)
#
# #5) Todo ZeroDivisionError:
#
# try:
#     x = 10
#     y = 0
#     print(x / y)  # Division by zero

# except zerodivisionerror as e:
#     print("zerodivision error:", e)
#
#Todo 3. Todo Handle an error with try-except-else.

# try:
#     # code that might raise an error
#     result = 5 / 0
#
# except zerodivisionerror:
#     # Code to handle the specific error (division by zero)
#     print("Error: Division by zero")
#
# else:
#     # Code to execute if no error occurred
#     print("Division successful. Result is:", result)

#Todo 4. Handle an error with try-except-else-finally.

# try:
#     result = 10 / 0  # This will raise a ZeroDivisionError
#
# except ZeroDivisionError:
#     print("Error: Division by zero!")
#
# else:
#     print("No error occurred!")
#
# finally:
#     print("This is the 'finally' block, on running mode...")


#Todo 5. Use raise for generating User Defined Exception for minimum length of a list should be 5.
#
# class minimumlength(Exception):
#     """Custom exception for minimum length of a list."""
#     pass

# def list(my_list):
#     min_length = 5
#     if len(my_list) < min_length:
#         raise minimumlength(f"List length must be at least {min_length}")
#
# # Example usage:
#
# try:
#     my_list = [1, 2, 3]
#     list(my_list)
#
# except minimumlength as e:
#     print(f"Error: {e}")
#
# else:
#     print("List has procced successfully.")


# Todo 6. Create a file 'mod.py' with a class with multiple methods and few member variables. Also create an individual
#  methods outside the class as well. Create  another file 'test.py' and without executing the 'mod.py' get it executed
#  using the  'test.py' file.







#Todo 7. Using the above mentioned files 'test.py' and 'mod.py'. In 'test.py' create an object
# of the class defined in the 'mod.py'. Call the methods using the object. Make sure
# only that class is accessible and not the individual method to execute.










# Todo 8. Using the files 'test.py' and 'mod.py' call the individual method which is defined outside the class in
#  'mod.py' and call in it test.py. Make sure only that method from the file 'mod.py' is accessible in 'test.py'.








#Todo 9. Create a package containing multiple modules. Import the package and use the
# features of the modules inside the package.






#Todo 10. Use the above package’s only one module.






#Todo 11. Use only specific class and methods of one of the module of the package.






#Todo 12.Create a script/program to open a file to write a string. Write a string in a file 'test_file.txt'.

# f=open("test_file.txt",'w')
# f_str=''' this is my content file
# here you can see the content of text_file  '''
#
# f.write(f_str)
# f.close()
#
#
# #Todo 13.Create a script/program to open a file 'test_file.txt' to read a string. Read the whole string content
# # from the file and print it.
#
# f=open('test_file.txt', 'r')
# file_content = f.read()          # Read the entire content of the file into a string
# print(file_content)                 # Print the content of the file
#
#
# #Todo 14.Create a script/program to open a file 'test_file.txt' to read the content line by line and print it.

# f=open('test_file.txt', 'r')
# for line in f:                  # Read the file line by line
#     print(line.strip())                #Print each linestrip() is used to remove any whitespace


# #Todo 15.Create a script/program to open a file 'test_file.txt' to append a string at the end of the existing string in a file.
#
# f=open('test_file.txt', 'a')
# string_to_append = input("Enter the string for append: ")
# f.write(string_to_append + "\n")         # Append the string to the file
# print("string append successfully.")


# #Todo 16.Create a script/program to write and read binary data in a file 'test_file.data'.
#
# f=open('test_file.data', 'wb')  # Write binary data to file
# binary_data = b'\x48\x65\x6C\x6C\x6F\x20\x57\x6F\x72\x6C\x64'  # Binary representation of "Hello World"
# f.write(binary_data)
#
# f=open('test_file.data', 'rb')      # Read binary data from file
# read_data = f.read()
#
# print("Binary Data read from file:", read_data)         # Display the binary data
# decoded_data = read_data.decode('utf-8')                # Convert binary data to string for display
# print("Decoded Binary Data:", decoded_data)
#

# #Todo 17. Using pickle dump no of variables with different data types in a file 'my_variables.data'.

# import pickle
#
# int = 42
# float = 3.14
# str = "Good Morning !"
# list = [1, 2, 3, 4, 5]
# dict = {'a': 1, 'b': 2, 'c': 3}
#
#
# f=open('my_variables.data', 'wb')   # Open a file in binary write mode
# pickle.dump(int,f)      #write a variables to the file
# pickle.dump(float,f)
# pickle.dump(str,f)
# pickle.dump(list,f)
# pickle.dump(dict,f)
# print("Convert text to byte stream to my_variables.data")


#Todo 18.Create another script/program and read the dumped variables in the file 'my_variables.data'

# import pickle
#
# int = 42
# float = 3.14
# str = "Good Morning !"
# list = [1, 2, 3, 4, 5]
# dict = {'a': 1, 'b': 2, 'c': 3}
#
#
# f=open('my_variables.data', 'wb')   # Open a file in binary write mode
# pickle.dump(int,f)      #write a variables to the file
# pickle.dump(float,f)
# pickle.dump(str,f)
# pickle.dump(list,f)
# pickle.dump(dict,f)
# print("Convert text to byte stream to my_variables.data")
#
# f=open('my_variables.data', 'rb')           #easy method for read a data
# data_read=f.read()
# print(data_read)

# f=open('my_variables.data', 'rb')
# list=pickle.load(f)                     #another method for read a data
# print(list)

# #Todo 19.Print the current date using datetime and date libraries.
#
# import datetime
#
# current_datetime = datetime.datetime.now()  # Get the current date and time
# current_date = datetime.date.today()        # Get the current date
# print("Current date & time:", current_datetime)   # Print the current date and time
# print("Current date:", current_date)    # Print the current date
# #
#
# #Todo 20.Convert a datetime to a string.
#
# from datetime import datetime
# my_datetime = datetime.now()
# my_datetime_str = my_datetime.strftime("%Y-%m-%d %H:%M:%S")         # Convert datetime to string
# print("Datetime in string format:", my_datetime_str)
#
# #Todo 21.Get the difference between two dates in days.
#
# from datetime import datetime
#
# date1 = datetime(2023, 1, 1)        # Declare two datetime objects
# date2 = datetime(2023, 2, 1)
#
# difference_in_days = (date2 - date1).days           # Get the difference between two dates in days
#
# print("Difference in days:", difference_in_days)


#Todo 22.Calculate your age in years, months and days.

# from datetime import datetime
#
# birth_date = datetime(2001, 4, 2)   # Date of birthdate
# current_date = datetime.now()   # Current date
#
# age = current_date - birth_date    #ifference between the current date and birth date
#
# years = age.days // 365         #My year, month & days from the age
# remaining_days = age.days % 365
# months = remaining_days // 30
# days = remaining_days % 30
#
# print(f"My age is approximately {years} years, {months} months, & {days} days.")

# #Todo 23.Get the date which is 1 week from today's date.
#
# from datetime import datetime, timedelta
#
# today = datetime.now()   #today's date
# one_week_from_now = today + timedelta(days=7)  #Add 7 days to today's date
#
# one_week_from_now = one_week_from_now.strftime('%Y-%m-%d')        # Format of date in  read format (YYYY-MM-DD)
# print("One week from today's date:", one_week_from_now)
#
# #Todo 24.Get the date which is 1 year from today's date.

# from datetime import datetime, timedelta
#
# today = datetime.now()      #today's date
# one_year_from_now = today + timedelta(days=365)  # Add 1 year to today's date The year has 365 days
# one_year_from_now = one_year_from_now.strftime('%Y-%m-%d')
# print("One year from today's date:", one_year_from_now)
#
#
# # #Todo 25.Get the date which is 1 month from today's date.
# #
# from datetime import datetime, timedelta
#
# today = datetime.now()
# one_month_from_now = today + timedelta(days=30) # Add 30 days to today's date
# one_month_from_now= one_month_from_now.strftime('%Y-%m-%d')
#
# print("One month from today's date:", one_month_from_now)
#
#
# # #Todo 26.Get the 1st day of the current month from today's date.
#
# from datetime import datetime
#
# today = datetime.now() #today's date
# first_day_of_month = today.replace(day=1) #the 1st day of the current month
# first_day_of_month= first_day_of_month.strftime('%Y-%m-%d')
#
# print("1st day of the current month:", first_day_of_month)
#
# # #Todo 27.Get the 1st month of the current year from today's date.
#
# from datetime import datetime
#
# today = datetime.now()
# first_month_of_current_year = today.replace(month=1, day=1)  #get 1st month of the current year
#
# # Format the date in a readable format (YYYY-MM-DD)
# first_month_of_current_year_formatted = first_month_of_current_year.strftime('%Y-%m-%d')
#
# print("1st month of the current year:", first_month_of_current_year_formatted)

# #Todo 28.Get the dates of current month starting from Monday to Sunday in a list.

# import calendar
# from datetime import datetime, timedelta
#
# today = datetime.now()
# first_day_of_month = today.replace(day=1)  #the first day of the current month
#
# # Get the weekday of the first day (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
# first_day_weekday = first_day_of_month.weekday()
#
# # Calculate the start of the week (Monday) by subtracting the weekday of the first day
# start_of_week = first_day_of_month - timedelta(days=first_day_weekday)
# week_dates = []     # A empty list to store the dates of the week
#
# # Add dates of the current week (Monday to Sunday) to the list
# for i in range(7):
#     week_dates.append(start_of_week + timedelta(days=i))
#
# for date in week_dates:         # Print the list of dates
#     print(date.strftime('%Y-%m-%d'))
#
# #Todo 29. Get the first date and last date of the current month.
#
# from datetime import datetime, timedelta
# today = datetime.now()
#
# first_date_of_month = today.replace(day=1)  #It shows the first date of month
#
# #It shows the last date of the current month
# last_date_of_month = first_date_of_month.replace(day=1, month=first_date_of_month.month+1) - timedelta(days=1)
#
# # Print the first and last dates of the current month
# print("First date of the current month:", first_date_of_month.strftime('%Y-%m-%d'))
# print("Last date of the current month:", last_date_of_month.strftime('%Y-%m-%d'))


#Todo 30.Get me the 1st and last date of the current month in the format as following. '14th June 2016 Tuesday 10:00:00 AM'

# from datetime import datetime, timedelta
#
# today = datetime.now()
# first_date_of_month = today.replace(day=1) #get first date of the current month
#
# # Get the last date of the current month
# last_date_of_month = first_date_of_month.replace(day=1, month=first_date_of_month.month+1) - timedelta(days=1)
#
# # Define a function to format the date
# def date(date):
#     suffix = 'th' if 11 <= date.day <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(date.day % 10, 'th')
#     return date.strftime(f"%d{suffix} %B %Y %A %I:%M:%S %p")
#
# # Format the first and last dates of the current month
# formatted_first_date = date(first_date_of_month)
# formatted_last_date = date(last_date_of_month)
#
# # Print the formatted dates
# print("First date of the current month:", formatted_first_date)
# print("Last date of the current month:", formatted_last_date)


#Todo 31.Get me random number from 1 to 100.

# import random
#
# random_number = random.randint(1, 100)
# print("Random number between 1 to 100:", random_number)
#
#
# #Todo 32.Get me a random combination of 4 different numbers between 1 to 100.
#
# import random
#
# random_com = random.sample(range(1, 101), 4)
# print("Random combination of 4 different numbers :", random_com)

#Todo 33.You have a sorted list from 1 to 10 you have to unsort it.

# import random
#
# # Create a sorted list from 1 to 10
# sorted_list = list(range(1, 11))
#
# # Shuffle the sorted list to unsort it
# random.shuffle(sorted_list)
#
# # Print the unsorted list
# print("Unsorted list:", sorted_list)


#Todo 34.Execute a shell script command from python code.

# import os
# print(os.name)
#
# os.system("ls")
# print(os.getcwd())
#
# os.system("cd")
# print(os.getcwd())
#
# command = "ls -l"
# os.system(command)  # Execute the shell command
#
# command="cat"
# os.system(command)
#
# #Todo 35.Create a regular expression to check a valid URL.
#
# import re
#
# def valid_url(url):
#     # Regular expression for a valid URL
#     pattern =re.compile(r'^(https?://)?(www\.)?\S+\.\S+$')
#     return bool(pattern.match(url))
#
# # Test the function with a URL
# url = "https://www.example.com"
# print(valid_url("www.skyscend bs.com"))
# print(valid_url("https://www.python.org/"))


#Todo 36. Create a regular expression to check a valid email.

# import re
# def valid_email(email):
#     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'  #Define the regular expression pattern
#
#     match = re.match(pattern, email)         # re.match() to check if the email matches the pattern
#     return bool(match)                       # Return True if there is a match, indicating a valid email address
#
# email = "user@example.com"
# if valid_email(email):
#     print(f"{email} is a valid email address.")
# else:
#     print(f"{email} is not a valid email address.")


#Todo 37. Create a regular expression to check a valid Pin code of India.

# import re
# def valid_pin(pin):
#     pattern = r'^[1-9][0-9]{5}$'
#     match = re.match(pattern, pin)
#
#     return bool(match)
#
# pin_check = "126777"
# if valid_pin(pin_check):
#     print(f"{pin_check} is a valid PIN code.")
# else:
#     print(f"{pin_check} is not a valid PIN code.")

#
# Todo 38. Create a class Student and add member variables with False values. The variables
# are as listed below. Marks will have a default value blank list.
# 1. Name
# 2. Reg No
# 3. Roll No
# 4. Standard
# 5. Admission Year
# 6. Marks
# 7. Result


# Add a constructor that will assign Name, Reg No, Roll No, Standard, Admission year. In the constructor add validation
# for Name to be only Alphabetic, Reg No to be alphanumeric, Roll No, Standard nad Admission year to be numeric. All abobve
# values will be accepted as string only. If the passed parameters are not string raise and Error to the user. Add a method that will accept a dictionary for marks containing subject as key and
# marks as values. It will add the dictionary to the list of marks. Marks list will have multiple elements and each element will be a dictionary only. Here there should be a
# validation to acccept the marks which are less than or equal to 100 only. If the obtained marks are less than 40 the result willl be fail otherwise pass. In the
# dictionary the result can be added.

class student:
    def __init__(self, name, reg_no, roll_no, standard, admission_year):
        self.Name = name
        self.RegNo = reg_no
        self.RollNo = roll_no
        self.Standard = standard
        self.AdmissionYear = admission_year
        self.Marks = []
        self.Result = False

        # Validations
        if not all(isinstance(attr, str) for attr in [name, reg_no, roll_no, standard, admission_year]):
            raise ValueError("All attributes must be strings.")
        if not name.isalpha():
            raise ValueError("Name must contain only alphabetic characters.")
        if not reg_no.isalnum():
            raise ValueError("Reg No must contain only alphanumeric characters.")
        if not (roll_no.isdigit() and standard.isdigit() and admission_year.isdigit()):
            raise ValueError("Roll No, Standard, and Admission Year must be numeric.")

    def add_marks(self, marks_dict):
        for subject, marks in marks_dict.items():
            if not isinstance(marks, int) or not (0 <= marks <= 100):
                raise ValueError("Marks must be integers between 0 and 100.")
            self.Marks.append({subject: marks, "Result": "Pass" if marks >= 40 else "Fail"})

    def calculate_grade(self, percentage):
        if percentage >= 95:
            return "O+"
        elif 90 <= percentage < 95:
            return "O"
        elif 85 <= percentage < 90:
            return "A+"
        elif 80 <= percentage < 85:
            return "A"
        elif 75 <= percentage < 80:
            return "B+"
        elif 70 <= percentage < 75:
            return "B"
        elif 60 <= percentage < 70:
            return "C"
        elif 50 <= percentage < 60:
            return "D"
        elif 40 <= percentage < 50:
            return "E"
        else:
            return "F"

    def generate_result(self):
        total_marks = 0
        total_passing_marks = 0
        total_obtained_marks = 0

        # print("*******************************************************************")
        print(f"Name : {self.Name}")
        print(f"Roll No : {self.RollNo} Standard: {self.Standard}")
        # print("*******************************************************************")
        print("Subject   Total Marks   Passing Marks   Obtained Marks   Result")

        for subject_data in self.Marks:
            subject, marks = list(subject_data.items())[0]
            total_marks += 100
            total_passing_marks += 40
            total_obtained_marks += marks
            print(f"{subject}        100            40               {marks}              {subject_data['Result']}")

        # print("*******************************************************************")

        print(f"TOTAL   {total_marks}   {total_passing_marks}   {total_obtained_marks}")
        result = "FAIL" if any(subject_data['Result'] == 'Fail' for subject_data in self.Marks) else "PASS"
        if result == "FAIL":
            print(f"Result: {result}")
        else:
            percentage = (total_obtained_marks / total_marks) * 100
            print(f"Result: {result} Percentage: {percentage}")
            grade = self.calculate_grade(percentage)
            print(f"Grade : {grade}")


student1 = student("Janvi", "A12345", "16", "10", "2022")
student1.add_marks({"Maths": 80, "Science": 65, "English": 35})
student1.generate_result()


#Todo  39. Optimize the following code and make it in two lines.
#     x = {'a':1, 'b':2} – No Change
#     if 'c' in x:
#         y = x['c']
#     else:
#         y = 0

# x = {'a': 1, 'b': 2}
# y = x.get('c', 0)

#
# Todo  40. Consider a variable which has string value “Skyscend Business Solutions Pvt Ltd.” print the following in one line.
#
#
# ◦ SKYSCEND
# ◦ Bus
# ◦ solutions
#
# text = "Skyscend Business Solutions Pvt. Ltd."
# print(text[:7].upper(), text[8:11].title(), text[12:21].lower())


#Todo 41. Create a function using 'lambda' for exponent of a given number. Take two arguments one as
# the number and the other one as the exponent

# expo = lambda num, exp: num ** exp
#
# result = expo(3, 3)  # Calculates 2 raised to the power of 3
# print(result)


#Todo 42. Create an assertion for a string to check the length of the string being minimum of 10 letters.

# def string(input_string):
#     assert len(input_string) >= 10, "String length must be at least 10 letters."
#
# input_string = "abcdefghij"
# string(string)  # This will pass because the length is 10 or more
#
# input_string = "abcdefghi"
# string(string)  # This will raise an AssertionError


#Todo 43. Read a file 'python.txt' which is containing python code and execute the python code which is read from the file.

# file_path = "python.txt"
#
# try:
#     with open(file_path, "r") as file:
#         python_code = file.read()
#
#     exec(python_code)   # Execute the Python code
#
# except FileNotFoundError:
#     print(f"File '{file_path}' not found.")
# except Exception as e:
#     print("An error occurred :", e)



#Todo 44. Using range get me a list of 1 to 10 and from this list generate a list as
# [13,15,17,19,21,23,25,27,29,31]. Code needs to be done in one line only.

# list = [x + 12 for x in range(1, 11)]
# print(list)


#Todo 45. Using range get me a list of even numbers between 1 to 100. Code needs to be done in one line only.

# even_num = [x for x in range(1, 101) if x % 2 == 0]
# print(even_num)


#Todo 46. Generate a list of exponents of first 25 integers. Code needs to be in one line only.

# list = [i ** 2 for i in range(1, 26)]
# print(list)

#Todo 47. Create a generator method to have the prime numbers using yield between 1 to 100.

# def prime():
#     for num in range(2, 101):
#         if all(num % i != 0 for i in range(2, int(num ** 0.5) + 1)):
#             yield num
#
# prime_generator = prime()
# for prime in prime_generator:
#     print(prime)
#

#Todo 48. Create a generator method which gives random numbers between 1 to 100 and the number not being repeated.
# Make sure it generates only 10 numbers.

# import random
# def generate_num():
#     numbers = set()
#     while len(numbers) < 10:
#         num = random.randint(1, 100)
#         if num not in numbers:
#             numbers.add(num)
#             yield num
#
# random_numbers_generator = generate_num()
# for random_number in random_numbers_generator:
#     print(random_number)


#Todo 49. Convert a decimal number '15' to binary, hexadecimal, octal numbers.

# decimal_num=15
#
# binary_num= bin(decimal_num)
# print("Binary:", binary_num)
#
# hexa_num = hex(decimal_num)
# print("Hexadecimal:", hexa_num)
#
# octal_num = oct(decimal_num)
# print("Octal:", octal_num)


#Todo 50. Convert a Hexadecimal number '10' to binary, decimal and octal numbers.

# hexa_num = '10'
#
# binary_number = bin(int(hexa_num, 16))
# print("Binary:", binary_number)
#
# decimal_num = int(hexa_num, 16)
# print("Decimal:", decimal_num)
#
# octal_num = oct(int(hexa_num, 16))
# print("Octal:", octal_num)


#Todo 51. Convert an Octal number '13' to binary, decimal and hexadecimal numbers.

# octal_num = '13'
#
# binary_num = bin(int(octal_num, 8))
# print("Binary:", binary_num)
#
# decimal_num = int(octal_num, 8)
# print("Decimal:", decimal_num)
#
# hexadecimal_num = hex(int(octal_num, 8))
# print("Hexadecimal:", hexadecimal_num)
#


#Todo 52. Convert Binary number '11010001111100111' to decimal, hexadecimal and octal numbers.

# binary_number = '11010001111100111'
#
# decimal_num = int(binary_num, 2)
# print("Decimal:", decimal_num)
#
# hexadecimal_num = hex(int(binary_num, 2))
# print("Hexadecimal:", hexadecimal_num)
#
# octal_number = oct(int(binary_number, 2))
# print("Octal:", octal_number)


#Todo 53. Create a dictionary containing all the Capital Letters 'A-Z', Small Letters 'a-z', and Digits '0-9'
# as keys and their ascii values as values using generators.

# ascii_dict = {chr(i): i for i in range(65, 91)}  # Capital Letters 'A-Z'
# ascii_dict.update({chr(i): i for i in range(97, 123)})  # Small Letters 'a-z'
# ascii_dict.update({chr(i): i for i in range(48, 58)})  # Digits '0-9'
#
# print(ascii_dict)

#Todo 54. Get an absolute value of any negative integer.

# negative_integer = -5
# absolute_value = abs(negative_integer)
#
# print("Absolute value:", absolute_value)

#Todo 55. Compare two numbers and get me the maximum number with a built-in function.

# number1 = 10
# number2 = 20
#
# max_num = max(number1, number2)
# print("Maximum number:", max_num)


#Todo 56. Create a class with member variables. Now perform the following.
# 1. Check whether an attribute exists in the class or not.
# 2. Fetch the value of an attribute of a class.
# 3. Update the value of an attribute of a class.
# 4. Delete the attribute of a class.

# class myclass:
#     def __init__(self):
#         self.attribute1 = "value1"
#         self.attribute2 = "value2"
#
# obj = myclass()
#
# # 1. Check whether an attribute exists in the class or not
# if hasattr(obj, 'attribute1'):
#     print("Attribute 'attribute1' exists in the class.")
# else:
#     print("Attribute 'attribute1' does not exist in the class.")
#
# # 2. Fetch the value of an attribute of a class
# value = getattr(obj, 'attribute1')
# print("Value of 'attribute1':", value)
#
# # 3. Update the value of an attribute of a class
# setattr(obj, 'attribute1', "new_value")
# print("Updated value of 'attribute1':", obj.attribute1)
#
# # 4. Delete the attribute of a class
# delattr(obj, 'attribute1')
# print("Attribute 'attribute1' deleted.")
#
# if hasattr(obj, 'attribute1'):      # Verify if attribute1 is deleted
#     print("Attribute 'attribute1' exists in the class.")
# else:
#     print("Attribute 'attribute1' does not exist in the class.")
#
# #Todo  57. Generate a list of having 10 elements using random but the numbers shoudl be either 1 or 0. Check if all the elements are 1 print “ALL” and if any of the single
# # element is 1 print “ANY” and if all the elements are 0 print “NONE”.
#
# import random
#
# random_list = [random.randint(0, 1) for _ in range(10)]
#
# if all(num == 1 for num in random_list):
#     print("ALL")
# elif any(num == 1 for num in random_list):
#     print("ANY")
# else:
#     print("NONE")
#
# print("Generate List:", random_list)
#
# #Todo 58. Get 10 random numbers in a list and get the maximum number from the list.
#
# import random
#
# random_num = random.sample(range(1, 101), 10)
# maximum_num = max(random_num)
#
# print("Random number:", random_num)
# print("Maximum number:", maximum_num)
#
#
# #Todo 59. Get 10 random numbers in a list and get the minimum number from the list.
#
# import random
#
# random_num = random.sample(range(1, 101), 10)
# minimum_num = min(random_num)
#
# print("Random numbers:", random_num)
# print("Minimum number:", minimum_num)
#
#
# #Todo 60. Get 10 random numbers from 1 to 100 in a list and create two separate lists from it for odd and
# # even numbers using filter.
#
# import random
#
# random_num = [random.randint(1, 100) for _ in range(10)]
# odd_num= list(filter(lambda x: x % 2 != 0, random_num))  #separate lists for odd and even numbers
# even_num = list(filter(lambda x: x % 2 == 0, random_num))
#
# print("Random numbers:", random_num)
# print("Odd numbers:", odd_num)
# print("Even numbers:", even_num)
#
#
# #Todo 61. Using map generate cubes of first 10 numbers.
#
# cubes = list(map(lambda x: x**3, range(1, 11))) #cubes of first num using map & lambda func
# print("Cubes of first 10 numbers:", cubes)
#
#
#
# #Todo 62. Using map generate a list from two lists by multiplying the elements in the two lists on the identical indexes
# # in both the lists.
#
# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 10]
#
# result_list = list(map(lambda x, y: x * y, list1, list2))
# print("Resulting list:", result_list)
#
#
# #Todo 63. Generate 15 random numbers from 1 to 100 and get the total of all these numbers.
#
# import random
#
# random_num = [random.randint(1, 100) for _ in range(15)]
# total = sum(random_num)
#
# print("Generated random numbers:", random_num)
# print("Total of all random numbers:", total)
#
#
# #Todo 64. Get a list of 10 random characters and then merge all the characters in a single string.
#
# import random
# import string
#
# random_char = [random.choice(string.ascii_letters) for _ in range(10)]
# merged_string = ''.join(random_char)
#
# print("Random characters list:", random_char)
# print("Merged string:", merged_string)
#
# #Todo 65. Create a class with few methods and in one of the method get all the global attributes that can be used in that method and also the local attributes that can beused in that method.
#
# class exampleclass:
#     global_attribute = "This is a global attribute"
#
#     def __init__(self, local_attribute):
#         self.local_attribute = local_attribute
#
#     def method1(self):
#         print("This is method 1")
#
#     def method2(self):
#         print("This is method 2")
#
#     def get_attributes(self):
#         print("Global attribute:", self.global_attribute)         # Accessing global attribute
#
#     local_attribute = "This is a local attribute"        # Accessing local attribute specific to this method
#     print("Local attribute:", local_attribute)
#
# example_instance = exampleclass("Local Attribute Value")        # Creating an instance of the class
# example_instance.get_attributes()                               # Calling the get_attributes method
#
# #Todo 66. Create two classes one as a parent and the other as a child. Make a validation whether the child is a
# # subclass of parent or not.
#
# class parentclass:
#     pass
#
# class childclass(parentclass):
#     pass
#
# if issubclass(childclass, parentclass):
#     print("ChildClass is a subclass of ParentClass")
# else:
#     print("ChildClass is not a subclass of ParentClass")
#
#
# #Todo 67. Get two lists ['a','b','c','d','e'],[1,2,3,4,5] and generate a single dictionary {'a':1,'b':2,'c':3,'d':4,'e':5} with the identical indexed items.
#
#
# keys = ['a', 'b', 'c', 'd', 'e']
# values = [1, 2, 3, 4, 5]
# result_dict = {key: value for key, value in zip(keys, values)}
#
# print(result_dict)

#Todo 68. Sort a list of random 25 numbers between 1 to 100 without using the sort method.

# import random
#
# random_num = [random.randint(1, 100) for _ in range(25)]
# print("Original list:", random_num)
#
# def bubble_sort(arr):       # Bubble sort implementation
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#
# bubble_sort(random_num)     # Sort the list using bubble sort
# print("Sorted list:", random_num)
#
# #Todo 69. Sort the following list with the second element of the inner list. [[4, ’a’], [9, ’x’], [10, ’c’], [25,’z’], [32, ‘b’]].
#
# my_list = [[4, 'a'], [9, 'x'], [10, 'c'], [25, 'z'], [32, 'b']]
# list = sorted(my_list, key=lambda x: x[1])
#
# print("Sorted list based on the second element:", list)
#
# #Todo 70. Create a function for addition of two numbers. Create a validation that both of them must be either float or integer using a built in method.
#
# def add(num1, num2):
#     if isinstance(num1, (int, float)) and isinstance(num2, (int, float)):
#         return num1 + num2
#     else:
#         raise TypeError("numbers must be float or integer.")
#
# try:
#     result = add(5, 1.5)        # Test the function
#     print("Result:", result)
# except TypeError as e:
#     print("Error:", e)

# try:                                def add()
#     result = add(5, '10.5')
#     print("Result:", result)
# except TypeError as e:
#     print("Error:", e)



#Todo 71. Create a function and a nested function inside this function. Assign variables outsie both the functions, define two variables inside the first function. Make on of
# the variables to be global. Define other two variable inside the nested function and make one of them global. Now call the locals() and globals() function from
# outside both the functions, inside first function and inside the nested function and check what is available as local and global variables which can be accessed.


# global_variable = "This is a global variable"
#
# def outer_fun():
#     outer_variable = "I am a variable in the outer function"
#
#     def nested_fun():
#         global nested_global_variable
#         nested_global_variable = "A global variable in nested function"
#         nested_variable = "I am a variable in the nested function"
#         print("Inside nested function locals:", locals())
#         print("Inside nested function globals:", globals())
#
#     nested_fun()
#     print("Inside outer function locals:", locals())
#     print("Inside outer function globals:", globals())
#
#
# outer_fun()
# print("Outside both functions locals:", locals())
# print("Outside both functions globals:", globals())
#
#
# Practicing a Lambda function

# add=lambda x,y=15, z=24: x+y+z
# print(add(20))

# def add(a,b):              # Add Function
#     return a+b
# print(add(3,8))
#
#
# add=lambda a,b:a+b
# print(add(2,3))        #Lambda Function


