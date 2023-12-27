class node:
    def __init__(self, value) -> None:
        self.next = None
        self.value = value

class stack_:
    def __init__(self):
        self.top = None
    
    def push(self, value):

        new_node = node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self, value):

        if self.top == None:
            return "Empty"
    
        self.top = self.top.next

    def peak(self):
        return self.top.value

    def isEmpty(self):
        return self.top == None

    def traverse(self):
        if self.top==None:
            return "empty"
        curr = self.top
        while curr!=None:
            print(curr.value)
            curr = curr.next
        

s = stack_()
s.push(1)
s.push(2)
s.push(3)        
s.push(4)

# print(s.peak())
s.traverse()