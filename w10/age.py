     #  class 
class Person ():
     def __init__(self, name,age):
          self.name = name
          self.age =age
     # try and except
     name = input("Please enter your name : ")
     try:
          age = int(input("Please enter age : "))
     except:
          print("ERROR!")
          age = int(input("Please enter your age L "))      
     # function
     def sarol(gender):
          print("sarol gender is" , gender)
     sarol("female")
     # display back
     print(f"Name : {name}")   
     print(f"Age : {age}")



