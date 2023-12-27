class MyBaseClass:
    def some_method(self):
        print("This is a method of the base class")

class MyDerivedClass(MyBaseClass):
    def some_method(self):
        super().some_method()  # Call the method of the base class without initializing it
        print("This is a method of the derived class")

# Create an instance of the derived class
obj = MyDerivedClass()

# Call the method of the derived class, which in turn calls the method of the base class
obj.some_method()
