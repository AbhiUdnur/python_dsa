class Bird:

    def flight(self):
        print("Most of the birds can fly but some can't")

class Sparrow(Bird):
    def flight(self):
        print("sparrows can fly")
    
class Ostrich(Bird):

    def flight(self):
        print("ostrich can't fly")  


b = Bird()
s = Sparrow()
o = Ostrich()

b.flight()
s.flight()
o.flight()
