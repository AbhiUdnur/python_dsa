class node:
    def __init__(self,value) :        

        self.next = None
        self.value = value

class que:
    def __init__(self) -> None:
        self.rear = None
        self.front = None
    
    def enqueue(self, value):
        new_node = node(value)
        if self.rear == None:
            self.rear=new_node
            self.front=new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
    def dequeue(self):
        if self.front == None:
            return "empty"

        else:
            self.front = self.front.next
    
    def isEmpty(self):

        return self.front == None

    def size(self):
        curr = self.front
        count=0
        while curr!= None:
            count+=1
            curr = curr.next
        return count

    def traverse(self):
        curr = self.front
        while curr != None:
            print(curr.value, end=" ")
            curr =curr.next
        print()

q = que()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)

q.traverse()
q.dequeue()
q.traverse()
