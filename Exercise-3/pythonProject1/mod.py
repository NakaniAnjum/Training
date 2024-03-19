

# Todo 6) Create a file 'mod.py' with a class with multiple methods and few member
# variables. Also create an individual methods outside the class as well.


# mod.py
class MyClass:
    def __init__(self, name):
        self.name = name
        self.count = 0

    def increment_count(self):
        self.count += 1

#Todo 8)  call the individual method which is defined outside the class in 'mod.py' and call in it test.py.
# Make sure only that method from the file 'mod.py' is accessible in 'test.py'.
def outside_method():
    print("outside method.")

