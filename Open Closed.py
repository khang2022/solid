"""Objects or entities should be open for extension but closed for modification.
"""


from abc import abstractclassmethod


# class StorageLocker():
#     def authenticate(self,client):
#      if   client == "aws":
#          pass
#             # Code to authenticate against aws
#      elif client == "azure":
#             # Code to authenticate against azure
#       elif client == "google cloud":
#             # Code to authenticate against azure       
      
            
#       return client   
#     def upload(self,filename):
#          if   client == "aws":
#           pass
#             # Code to upload a file to aws
#          elif client == "azure":
#             # Code to upload a file to azure
#            elif client == "google cloud":
#             # Code to upload a file to azure   
            
            
            



from abc import ABC ,abstractmethod

class Auth(ABC):
    @abstractclassmethod
    def authenticate(self):
        pass
    
 class Uploader(ABC):
     @abstractclassmethod
     def upload_file(self):
         pass
 
 class Aws(Auth,Uploader):
     
     def authenticate(self):
         # code to authenticate against aws
         return auth_client
     def upload_file(self,filename):
         return status_code       
    

 class azure(Auth,Uploader):
     
     def authenticate(self):
         # code to authenticate against aws
         return auth_client
     def upload_file(self,filename):
         return status_code 
 
  class Googlecloud(Auth,Uploader):
     
     def authenticate(self):
         # code to authenticate against aws
         return auth_client
     def upload_file(self,filename):
         return status_code      
               
"""
https://www.geeksforgeeks.org/abstract-classes-in-python/#:~:text=An%20abstract%20class%20can%20be
,is%20called%20an%20abstract%20class.

"""    
        