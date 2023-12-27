class MyClass: 
	
	__hiddenVariable = 5
	def add(self, increment): 
		self.__hiddenVariable += increment 
		print (self.__hiddenVariable) 

myObject = MyClass()	 
myObject.add(2) 
 
# print (myObject.__hiddenVariable) 
