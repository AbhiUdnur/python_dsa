# class base:
    
#     class_variable = "I am a class variable"

#     def __init__(self) :
#         pass
    
#     @classmethod
#     def _classmethod(cls):
#         print(cls.class_variable)
    
#     @ staticmethod
#     def static_methodO():
#         print("this is static method")

# c = base()
# c._classmethod()
# c.static_methodO()

# Python program to demonstrate
# use of class method and static method.
from datetime import date

class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	@classmethod
	def fromBirthYear(cls, name, year):
		return cls(name, date.today().year-year)

person1 = Person('mayank', 21)
person2 = Person.fromBirthYear('mayank', 1996)

print(person1.age)
print(person2.age)

