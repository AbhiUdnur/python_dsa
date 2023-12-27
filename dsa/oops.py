class MathOperations:
    

    def add(self, x, y, z):
        return x + y + z
    def add(self, x, y):
        return x + y

# Create an instance of the class
math_obj = MathOperations()

# Call the overloaded methods
result1 = math_obj.add(2, 3)
result2 = math_obj.add(2, 3, 4)

print(result1)  # Output: Error - The second add method is the one defined in the class
print(result2)  # Output: 9
