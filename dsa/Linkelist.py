class node:
    def __init__(self, value) :
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self) -> None:
        self.head = None
        self.n = 0
    
    def insert_head(self, value):
        new_node = node(value)
        new_node.next = self.head
        self.head = new_node
        self.n+=1
    
    def append(self,value):
        
        new_node = node(value)
        if self.head == None:
          self.head = new_node
          return
        
        curr = self.head
        while curr.next!= None:
            curr = curr.next
        
        curr.next = new_node
        self.n+=1
    
    def __len__(self):
        return self.n

    def del_head(self):
        
        if self.head == None:
            return "empty"
        else:
            self.head = self.head.next

    def pop(self):
        curr = self.head
        if self.head == None:
            return "empty"
        
        if curr.next== None:
            self.del_head()
            self.n -=1
            return
        
        while curr.next.next !=None:
            curr = curr.next
        curr.next = None
        self.n-=1
        return

    def traverse(self):
        curr = self.head
        result=''
        while curr!= None:
            result = result + str(curr.value)+"->"
            curr = curr.next
        return result[:-2]
    
    def clear(self):
        self.head= None
        self.n=0

L = LinkedList()

L.append(1)
L.append(2)
L.append(3)
L.append(4)
print(L.traverse())
L.insert_head(5)
print(L.traverse())
L.pop()
print(L.traverse())
L.clear()
print(L.traverse())
