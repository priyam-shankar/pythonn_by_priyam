#abc module => abstraction based classes module
#ABC => abstarction based classes , classes in which we used in inheritance
from abc import ABC, abstractmethod

class Animal(ABC):          #abstract class
    
    @abstractmethod
    def make_sound(self):       # functon which we not gonna to implement ==> abstarct method ==> for this we use a decorator from same module = abstarctmethod
        pass
    
class Lion(Animal):
    def make_sound(self):
        print("Roar!")
        
class Cow(Animal):
    def make_sound(self):
        print("Moo!")
        
lion = Lion()
lion.make_sound()

cow = Cow()
cow.make_sound()
           