class person(object):
    def __init__(self,name,IDnum) :

        self.name = name 
        self.IDnum = IDnum 

    def display(self):
        print(self.IDnum)
        print(self.name)
    
class employee(person):
    def __init__(self, name, IDnum, salary, post) -> None:
        self.salary = salary
        self.post = post
        person.__init__(self, name, IDnum)

    def details(self):
        print(self.name)
        print(self.IDnum)
        print(self.post)
        

class company(employee):
   def __init__(self, name, IDnum, company_name) -> None:
        person.__init__(self,name, IDnum)
        self.company_name = company_name
  
   def display(self):
        print(self.company_name)
        print(self.name)
        print(self.IDnum)

a = company("iFJ", "8689", "CODITAS")
a.display()