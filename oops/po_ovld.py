class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Overloading the + operator
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        # Overloading the == operator
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

# Create instances of the Point class
point1 = Point(1, 2)
point2 = Point(3, 4)

# Using the overloaded + operator
result = point1 + point2
print(result)  # Output: Point(4, 6)

# Using the overloaded == operator
print(point1 == point2)  # Output: False
