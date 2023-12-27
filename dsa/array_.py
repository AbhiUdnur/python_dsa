import ctypes

class myArray():

  def __init__(self):
    self.size = 1
    self.n = 0
    self.A = self._make_array(self.size)

  def _make_array(self,capacity):
    return (capacity*ctypes.py_object)()

  def __len__(self):
    return self.n

  def append(self, item):
    if self.n == self.size:
      self._resize(self.size*2)
    
    self.A[self.n] = item
    self.n +=1

  def _resize(self, new_capacity):
    B = self._make_array(new_capacity)
    self.size = new_capacity
    for i in range(self.n):
      B[i] = self.A[i]

    self.A = B

  def __str__(self):
    result = ''
    for i in range(self.n):
      result = result+str(self.A[i])+","
    
    return "[ "+result[:-1]+" ]"

  def __getitem__(self,index):
    if 0<= index <self.n:
      return self.A[index]
    else:
      return "Index error - list index out of range"

  def pop(self):
    if self.n==0:
      return "emplty list"
    print(self.A[self.n-1])
    self.n = self.n-1
  
  def clear(self):
    self.n = 0
    self.size = 1
  
  def insert(self, pos, item):
    if self.n == self.size:
      self._resize(self.size*2)
    
    for i in range(self.n,pos,-1 ):
      self.A[i] = self.A[i-1]
    
    self.A[pos] = item
    self.n +=1
  
  def __delitem__(self, pos):
    for i in range(pos, self.n-1):
      self.A[i] = self.A[i+1]
    self.n-=1
  
  def find(self,item):
    for i in range(self.n):
      if self.A[i] == item:
        return i
    
    return "not in list"
  
  def remove(self, item):
    pos = self.find(item)
    if type(pos) == int:
      return self.__delitem__(pos)
    return pos


L = myArray()

L.append("UH")
L.append(4)
L.append(True)
L.append(1.78)

print(L)