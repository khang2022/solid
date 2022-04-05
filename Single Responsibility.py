""" A class should have one and only one reason to change,
      meaning that a class should have only one job.
"""

class Books:
    def __init__(self):
        self.books = {}
        self.number = 0
    
    def add_book(self,book):
        self.number +=1
        self.books[self.number] = book
    
    def __str__(self):
        return str(self.books) 
       
            
b = Books()
b.add_book("Book A")
b.add_book("Book B")
print(f"The books i have read is that {b}")









# class Books:
#     def __init__(self):
#         self.books = {}
#         self.number = 0
    
#     def add_book(self,book):
#         self.number +=1
#         self.books[self.number] = book
    
#     def __str__(self):
#         return str(self.books) 
    
#     def store_books(self,filename):
#         with open(filename,"w") as f:
#             f.write(str(self.books))
       
            
# b = Books()
# b.add_book("Book A")
# b.add_book("Book B")
# print(f"The books i have read is that {b}") 
# b.store_books("filename.txt")    






# class Books:
#     def __init__(self):
#         self.books = {}
#         self.number = 0
    
#     def add_book(self,book):
#         self.number +=1
#         self.books[self.number] = book
    
#     def __str__(self):
#         return str(self.books) 

# class StoreBook():
#     @staticmethod    
#     def store_books(self,filename):
#         with open(filename,"w") as f:
#             f.write(str(self.books))
       
            
# b = Books()
# b.add_book("Book A")
# b.add_book("Book B")
# print(f"The books i have read is that {b}") 

# s = StoreBook():
# s.store_books("filename.txt")    





"""https://www.programiz.com/python-programming/methods/built-in/staticmethod
#:~:text=What%20is%20a%20static%20method,the%20state%20of%20the%20object."""