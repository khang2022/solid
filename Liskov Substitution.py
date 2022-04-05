"""The Liskov Substitution Principle states that subclasses should be substitutable for their base classes.

This means that, given that class B is a subclass of class A, we should be able to pass 
an object of class B to any method that expects an object of class A
and the method should not give any weird output in that case.

https://www.freecodecamp.org/news/solid-principles-explained-in-plain-english/

"""

class KitchenAppliance():
    def on():
        pass
    
    def off():
        pass
    
    def set_temperature():
        pass
    
class Toaster(KitchenAppliance):
    def on():
        # code to turn on toaster
    def off():
        # code to turn off toaster
    def set_temperature():
        # code to set temp on toaster

class Juicer(KitchenAppliance):
      def on():
        # code to turn on Juicer
    def off():
        # code to turn off Juicer
    def set_temperature():
        # code to set temp on toaster!    @@   
        
        



class KitchenAppliance():
    def on():
        pass
    
    def off():
        pass       
  
 
 
class KitchenAppliancewithTemp(KitchenAppliance):
    def set_temperature():
        pass
     
        
                   