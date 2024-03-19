#Todo 1. Get me list of odd numbers between 1 to 20 without using if condition.

# odd_num= [num for num in range(1, 21) if num % 2 != 0]
# print(odd_num)

#Todo 2.Get a list of 1 to 20 then remove elements from list to get only even elements.

# num= list(range(1, 21))
# even_num = [num for num in numbers if num % 2 == 0]
# print(even_num)


#Todo 3. Get a list of 1 to 8 and then 4 to 10. Get the common elements from both the list in  a new list.

# num1=list(range(1,9))
# num2=list(range(4,11))
#
# common_elements = list(set(num1).intersection(set(num2)))
# print(common_elements)
# print(num1)

'''4. Sort a shuffled list of 10 random numbers in descending order.         '''

# import random
# random_num = [random.randint(1, 100) for _ in range(10)]
#
# # Shuffle the list
# random.shuffle(random_num)
#
# # Sort the shuffled list in descending order
# random_num.sort(reverse=True)
#
# print(random_num)

'''5    x=(1,2,3,4,5), y=(4,5,6,7)..
 # Combine these two tuples in a single tuple ignoring the  common elements.'''

# x = (1, 2, 3, 4, 5)
# y = (4, 5, 6, 7)
#
# result_tuple = tuple(set(x).union(y))
# print(result_tuple)

'''6. Define two sets and perform all the set operations and validation operations.'''

# def main():
#     # Define two sets
#     set_A = {1, 2, 3, 4, 5}
#     set_B = {4, 5, 6, 7, 8}
#
#     # Perform set operations
#     union_set = set_A.union(set_B)
#     intersection_set = set_A.intersection(set_B)
#     difference_set_A_B = set_A.difference(set_B)
#     difference_set_B_A = set_B.difference(set_A)
#     symmetric_difference_set = set_A.symmetric_difference(set_B)
#
#     # Perform validation operations
#     is_subset_A_B = set_A.issubset(set_B)
#     is_subset_B_A = set_B.issubset(set_A)
#     is_superset_A_B = set_A.issuperset(set_B)
#     is_superset_B_A = set_B.issuperset(set_A)
#     are_disjoint = len(set_A.intersection(set_B)) == 0
#
#     # Print results
#     print("Set A:", set_A)
#     print("Set B:", set_B)
#     print("\nSet Operations:")
#     print("Union:", union_set)
#     print("Intersection:", intersection_set)
#     print("Set difference (A - B):", difference_set_A_B)
#     print("Set difference (B - A):", difference_set_B_A)
#     print("Symmetric difference:", symmetric_difference_set)
#     print("\nValidation Operations:")
#     print("Is A a subset of B?", is_subset_A_B)
#     print("Is B a subset of A?", is_subset_B_A)
#     print("Is A a superset of B?", is_superset_A_B)
#     print("Is B a superset of A?", is_superset_B_A)
#     print("Are A and B disjoint?", are_disjoint)
#
# if __name__ == "__main__":
#     main()

'''' 7. Generate a dictionary {1:1,2:1,3:1,4:1,...,10:1} in one line using dictionary's method.'''

# my_dict = {key: 1 for key in range(1, 11)}
# print(my_dict)

'''8. Print all the keys and values of a dictionary.'''

# my_dict = {'a': 1, 'b': 2, 'c': 3}
# for key in my_dict:
#     print("Key:", key, "Value:", my_dict[key])


''' 9. Two dictionaries {'a':1,'b':2,'c':3}, {'a':4,'d':5,'e':6}. Merge these two dictionaries.'''


# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'a': 4, 'd': 5, 'e': 6}
# dict1.update(dict2)
# print("Merged dictionary:", dict1)


''' 10. How to check whether a key is existing in a dictionary or not.'''

# dict = {'a': 1, 'b': 2, 'c': 3}
#
# if 'a' in dict:
#     print("'a' is a key in the dictionary.")
# else:
#     print("'a' is not a key in the dictionary.")
#
# if 'd' in dict:
#     print("'d' is a key in the dictionary.")
# else:
#     print("'d' is not a key in the dictionary.")
#

'''11. How can we have two variables refering to a single list, set and dictionary.'''


# FOR LISTS

# Creating a list
# list = [1, 2, 3, 4]
#
# # Creating another variable referring to the same list
# another_list = list
#
# # Modifying the list using one of the variables
# list.append(5)
#
# # Both variables refer to the same list, so changes are reflected in both
# print(list)
# print(another_list)
#
#
# # FOR SETS
#
# # Creating a set
# set = {1, 2, 3}
#
# # Creating another variable referring to the same set
# new_set = set
#
# # Modifying the set using one of the variables
# set.add(7)
#
# # Both variables refer to the same set, so changes are reflected in both
# print(set)
# print(new_set)

#
# # FOR DICTIONARY

# # Creating a dictionary
# dict = {'a': 2, 'b': 3}
#
# # Creating another variable referring to the same dictionary
# new_set_dict = dict
#
# # Modifying the dictionary using one of the variables
# dict['c'] = 4
#
# print(dict)
# print(new_set_dict)

'''12. Use all the case methods of strings.'''

# my_string = "HIIIIIII MYYyyYyy Nameee is AnjUMMM"
#
# print("lowercase:", my_string.lower())
# print("uppercase:", my_string.upper())
# print("capital:", my_string.capitalize())
# print("Title:", my_string.title())
# print("swap:", my_string.swapcase())

# '''13. How to split a string with a substring '''

# string = "Hello Good Morning !!!!! Hello World!"
# substring = "World"
# split= string.partition(substring)
# print(split)


'''14. How to replace a string with a substring?'''''
#
# string = "Hello World! Good Morning to everyone, start new day !"
# old_substring = "World"
# new_substring = "Universe"
# new_string = string.replace(old_substring, new_substring)
# print(new_string)

'''15. How to join multiple strings with a substring?'''''

# strings = ["apple", "banana", "orange"]
# substring = ", "
# result = substring.join(strings)
# print(result)

'''16. How to make partition of a string?'''

# string = "Hello, world! This is a sample string. Hello again, world!"
# separator = "sample"
# part1, separator_found, part2 = string.partition(separator)
#
# print("Part 1:", part1)
# print("Separator found:", separator_found)
# print("Part 2:", part2)
#

'''17. How to find the no of occurences of a substring?'''

# string = "Hiiiiii !!!!Today is a great day"
# substring = "Hello"
# occurrences = string.count(substring)
# print("number of occurrences:", occurrences)


'''18. Use all the validation methods used with string.'''''

# 1) isalnum()

# a = "Hiiii111 "
# print(a.isalnum())  # True
#
# a = "heyy "
# print(a.isalnum())  # False
#
# #2) isalpha()
#
# a = "kkkk"
# print(a.isalpha())  # True
#
# a = "Hello123"
# print(a.isalpha())  # False
#
# #3) isdigit():
#
# a = "123"
# print(a.isdigit())  # True
#
# a = "123abc"
# print(a.isdigit())  # False
#
#
# #4) islower()
#
# a = "hello"
# print(a.islower())  # True
#
# a = "Hello"
# print(a.islower())  # False
#
#
# #5) isupper()
#
# a = "HELLO"
# print(a.isupper())  # True
#
# a = "Hello"
# print(a.isupper())  # False
#
# #6) isspace()
#
# a = "   "
# print(a.isspace())  # True
#
# a = "  good girl  "
# print(a.isspace())  # False

'''19. Convert all the data structures to other data structures.'''''

#Convert list to tuple

# my_list = [1, 2, 3]
# my_tuple = tuple(my_list)
#
# # Convert list to set
# my_set = set(my_list)
#
# # Convert list to dictionary (assuming list contains key-value pairs)
# my_list_of_tuples = [(1, 'a'), (2, 'b'), (3, 'c')]
# my_dict = dict(my_list_of_tuples)
#
# # Convert list to string
# my_string = ''.join(map(str, my_list))
#
# #Convert a tuple to other data structures:
#
# # Convert tuple to list
# my_tuple = (1, 2, 3)
# my_list = list(my_tuple)
#
# # Convert tuple to set
# my_set = set(my_tuple)
#
# # Convert tuple to dictionary (assuming tuple contains key-value pairs)
# my_tuple_of_tuples = ((1, 'a'), (2, 'b'), (3, 'c'))
# my_dict = dict(my_tuple_of_tuples)
#
# # Convert tuple to string
# my_string = ''.join(map(str, my_tuple))
#
# #Convert a set to other data structures:
#
# # Convert set to list
# my_set = {1, 2, 3}
# my_list = list(my_set)
#
# # Convert set to tuple
# my_tuple = tuple(my_set)
#
# # Converting set to dictionary is not straightforward as sets are unordered collections
# # Convert set to string
# my_string = ''.join(map(str, my_set))
#
# #Convert a dictionary to other data structures
#
# # Convert dictionary to list of keys, values, or items
# my_dict = {1: 'a', 2: 'b', 3: 'c'}
# my_keys = list(my_dict.keys())
# my_values = list(my_dict.values())
# my_items = list(my_dict.items())
#
# # Convert dictionary to tuple of keys, values, or items
# my_keys_tuple = tuple(my_dict.keys())
# my_values_tuple = tuple(my_dict.values())
# my_items_tuple = tuple(my_dict.items())
#
# # Convert dictionary to set of keys, values, or items
# my_keys_set = set(my_dict.keys())
# my_values_set = set(my_dict.values())
# my_items_set = set(my_dict.items())
#
# # Convert dictionary to string
# my_string = str(my_dict)
#
# #Convert a string to other data structures:
#
# # Convert string to list of characters
# my_string = "Hello"
# my_list = list(my_string)
#
# # Convert string to tuple of characters
# my_tuple = tuple(my_string)
#
# # Convert string to set of unique characters
# my_set = set(my_string)
#
# # Convert string to dictionary (not common)
# # In this example, each character in the string is treated as a key with a default value
# my_dict = dict.fromkeys(my_string, 0)
#

'''20. Get the last element of the list, tuple and string.'''

# list = [1, 2, 3, 4, 5]
# element = list[-1]
# print(element)
#
# #Tuple:
#
# tuple = (1, 2, 3, 4, 5)
# element = tuple[-1]
# print(element)
#
# #string:
#
# string = "Hello"
# character = string[-1]
# print(character)



'''21. Get last 3 elements of the list, tuple and string.'''

#list:

# list = [1, 2, 3, 4, 5]
# elements = list[-3:]
# print(elements)
#
# #Tuple:
#
# tuple = (1, 2, 3, 4, 5)
# elements = tuple[-3:]
# print(elements)
#
# # string:
#
# string = "Hello"
# characters = string[-3:]
# print(characters)

'''22. Get first 5 elements of list, tuple and string.'''''

#list:

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# elements = list[:5]
# print(elements)
#
# #Tuple:
#
# tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# elements = tuple[:5]
# print(elements)
#
#
# #string:
#
# string = "Hello GOOD Morning !!!"
# characters = string[:5]
# print(characters)


'''23. Get all the elements excluding first and last elements from list, tuple and string.'''''

#List:

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# elements = list[1:-1]
# print(elements)
#
# #Tuple:
#
# tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# elements = tuple[1:-1]
# print(elements)
#
# #string:
#
# string = "Hello World!"
# characters = string[1:-1]
# print(characters)


'''24. Get all the elements in a list using : operator.'''

# list = [1,3, 8, 9, 10,11,24,12,34,45,]
# elements = list[:]
# print(elements)

'''25. Get last 5 elements from a list of 1 to 10 using negative indexing.'''

# numbers=list(range(1,11))
# last_5_elements = numbers[-5:]
# print("Last 5 elements:", last_5_elements)
#

'''26. Get 4 elements of the list excluding last 2 elements using negative indexing.'''''
#
# my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# result = my_list[-6:-2]
# print("Result:", result)


''''27. Convert a list of tuple to dictionary.'''

# list_of_tuples = [(1, 'apple'), (2, 'banana'), (3, 'orange')]
# dict = dict(list_of_tuples)
# print(dict)


#Todo 28. Create a dictionary using range() as following. #{'a':1, 'b':2, 'c':3, 'd':4, 'e':5....'y':25,'z':26}.
#
# dict = {chr(i): i - 96 for i in range(97, 123)}
# print(dict)


''''29. There are two lists [1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20].'''''
        #Get a third list from these two lists as [12,14,16,18,20,22,24,26,28,30].'''


# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# list2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#
# result_list = [x + y for x, y in zip(list1, list2)]
# print(result_list)


''''30. Get Square of all the elments in a list from 1 to 10 numbers.'''

# square_list = [x**2 for x in range(1, 11)]
# print(square_list)

#Todo 31. There are two lists [1,2,3,4,5], [4,5,6,7] get a list from these two lists [1,2,3,6,7].

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7]
#
# result_list = [x for x in list1 if x not in list2] + list2
# print(result_list)


#Todo 32. Fetch the data from the following.


'''1. Fetch 5 which is the value of ‘e’ from below which is marked in red.
x = {‘a’:1, ‘b’:2, ‘c’:3,’d’:[1,2,3,4,(5.6.7,{‘e’:5})]}'''


x = {'a': 1, 'b': 2, 'c': 3, 'd': [1, 2, 3, 4, (5, 6, 7, {'e': 5})]}
e_value = x['d'][4][3]['e']
print(e_value)


#Todo 2. Fetch 2 from below which is marked in red.

'''x = {‘a’:{‘b’:[1,2,(3,4,{‘c’:3,’d’:4,’e’:[1,2,3]})]}'''''


# x = {'a': {'b': [1, 2, (3, 4, {'c': 3, 'd': 4, 'e': [1, 2, 3]})]}}
# c = x['a']['b'][2][2]['c']
# print(c)


#Todo 3. Fetch 6 from below which is marked in red.

'''x = [1, 2, (3, 4, 5, {‘a’:1, ‘b’:[2,3,4,(5,6)]})]'''


# x = {'a': {'b': [1, 2, (3, 4, {'c': 3, 'd': 4, 'e': [1, 2, 3]})]}}
# c = x['a']['b'][2][2]['c']
# print(c)


#Todo 4. Fetch 2 from above which is marked in red.

'''x = {True:[1,2,3,{‘a’:1,’b’:2}],False:[(2,3,4,5,{1:2})]}'''

# x = {True: [1, 2, 3, {'a': 1, 'b': 2}], False: [(2, 3, 4, 5, {1: 2})]}
# true_value= x[True]
# print(true_value)


#Todo 5. Fetch 9 from above which is marked in red.

# '''x = {1:2,2:3,3:4,4:{‘a’:’b’,’c’:’d’,’e’:’f’,’f’:[1,2,3,{1:9,3:8}]}'''
#
# x = {1: 2, 2: 3, 3: 4, 4: {'a': 'b', 'c': 'd', 'e': 'f', 'f': [1, 2, 3, {1: 9, 3: 8}]}}
# value = x[4]['f']
# print(value)

'''33. Create a function for string that will check whether a string is having the first
letter as Capital and not anyother letter is capital.'''''


# def capital(string):
#     # Check if the first letter is capitalized and no other letter is capitalized
#     return string[0].isupper() and not any(char.isupper() for char in string[1:])

# Test the function
# print(capital("Hello"))     # False
# print(capital("hello"))     # False
# print(capital("hELLO"))     # False
# print(capital("HeLlo"))     # False
# print(capital("HeLlo World"))   # False
# print(capital("Hello world"))   # True
# print(capital("Hello World"))   # False



''''Todo 34 Create a class Student and add member variables with False values. The variables are as listed below. Marks will have a default value blank list.
1. Name
2. Reg No
3. Roll No
4. Standard
5. Admission Year
6. Marks
7. Result '''''


'''Add a constructor that will assign Name, Reg No, Roll No, Standard, Admission
year. In the constructor add validation for Name to be only Alphabetic, Reg No to be
alphanumeric, Roll No, Standard nad Admission year to be numeric. All abobve
values will be accepted as string only.
Add a method that will accept a dictionary for marks containing subject as key and
marks as values. It will add the dictionary to the list of marks. Marks list will have
multiple elements and each element will be a dictionary only. Here there should be a
validation to acccept the marks which are less than or equal to 100 only. If the
obtained marks are less than 40 the result willl be fail otherwise pass. In the
dictionary the result can be added.
Add another method that will generate the result. This method will check if there
is any line in the marks having fail as result the result will be Fail and it will print the
complete result as following.


Name : <Student Name>
Roll No : <Roll No> Standard: <Standard>


Subject Total Marks Passing Marks Obtained Marks Result
<Sub 1> 100 40 <obtained marks> <result>
<Sub 1> 100 40 <obtained marks> <result>
<Sub 1> 100 40 <obtained marks> <result>


TOTAL <total> <total> <total>
Result: PASS / FAIL Percentage: <percentage>'''


# class student:
#     def __init__(self, name, reg_no, roll_no, standard, admission_year):
#         self.nameame = name
#         self.regNoegNo = reg_no
#         self.rollNoo = roll_no
#         self.standard = standard
#         self.admissionyear = admission_year
#         self.marks = []
#         self.result = False
#
#
#         if not self.name.isalpha():
#             raise ValueError("Name must contain only alphabetic characters.")
#         if not self.regNo.isalnum():
#             raise ValueError("Reg No must contain only alphanumeric characters.")
#         if not (self.rollNo.isdigit() and self.standard.isdigit() and self.admissionyear.isdigit()):
#             raise ValueError("Roll No, Standard, and Admission Year must be numeric.")
#
#     def add_marks(self, marks_dict):
#         for subject, marks in marks_dict.items():
#             if not isinstance(marks, int) or not (0 <= marks <= 100):
#                 raise ValueError("Marks")
#             self.Marks.append({subject: marks, "Result": "Pass" if marks >= 40 else "Fail"})
#
#     def generate_result(self):
#         total_marks = 0
#         total_passing_marks = 0
#         total_obtained_marks = 0
#
#         print(f"Name: {self.Name}")
#         print(f"Roll No: {self.RollNo} Standard: {self.Standard}")
#         print("\nSubject   Total Marks   Passing Marks   Obtained Marks   Result")
#
#         for subject_data in self.Marks:
#             subject, marks = list(subject_data.items())[0]
#             total_marks += 100
#             total_passing_marks += 40
#             total_obtained_marks += marks
#             print(f"{subject}        100            40               {marks}              {subject_data['Result']}")
#
#         print(f"\nTOTAL   {total_marks}   {total_passing_marks}   {total_obtained_marks}")
#         result = "FAIL" if any(subject_data['Result'] == 'Fail' for subject_data in self.Marks) else "PASS"
#         percentage = (total_obtained_marks / total_marks) * 100
#         print(f"Result: {result} Percentage: {percentage:.2f}%")
#
#
# # Example usage:
# student1 = Student("John Doe", "A12345", "123", "10", "2022")
# student1.add_marks({"Maths": 80, "Science": 65, "English": 35})
# student1.generate_result()


# class Student:
#     def __init__(self, name, reg_no, roll_no, standard, admission_year):
#         self.Name = name
#         self.RegNo = reg_no
#         self.RollNo = roll_no
#         self.Standard = standard
#         self.AdmissionYear = admission_year
#         self.Marks = []
#         self.Result = False
#
#         # Validations
#         if not self.Name.isalpha():
#             raise ValueError("Name must contain only alphabetic characters.")
#         if not self.RegNo.isalnum():
#             raise ValueError("Reg No must contain only alphanumeric characters.")
#         if not (self.RollNo.isdigit() and self.Standard.isdigit() and self.AdmissionYear.isdigit()):
#             raise ValueError("Roll No, Standard, and Admission Year must be numeric.")
#
#     def add_marks(self, marks_dict):
#         for subject, marks in marks_dict.items():
#             if not isinstance(marks, int) or not (0 <= marks <= 100):
#                 raise ValueError("Marks must be integers between 0 and 100.")
#             self.Marks.append({subject: marks, "Result": "Pass" if marks >= 40 else "Fail"})
#
#     def generate_result(self):
#         total_marks = 0
#         total_passing_marks = 0
#         total_obtained_marks = 0
#
#         print(f"Name: {self.Name}")
#         print(f"Roll No: {self.RollNo} Standard: {self.Standard}")
#         print("\nSubject   Total Marks   Passing Marks   Obtained Marks   Result")
#
#         for subject_data in self.Marks:
#             subject, marks = list(subject_data.items())[0]
#             total_marks += 100
#             total_passing_marks += 40
#             total_obtained_marks += marks
#             print(f"{subject}        100            40               {marks}              {subject_data['Result']}")
#
#         print(f"\nTOTAL   {total_marks}   {total_passing_marks}   {total_obtained_marks}")
#         result = "FAIL" if any(subject_data['Result'] == 'Fail' for subject_data in self.Marks) else "PASS"
#         percentage = (total_obtained_marks / total_marks) * 100
#         print(f"Result: {result} Percentage: {percentage:.2f}%")
#
# student1 = Student("John Doe", "A12345", "123", "10", "2022")
# student1.add_marks({"Maths": 80, "Science": 65, "English": 35})
# student1.generate_result()


#