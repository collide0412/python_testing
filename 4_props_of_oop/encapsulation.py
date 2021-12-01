class Animal:
    def __init__(self, type, country):
        self.type = type
        self.country = country             
        
    def description(self):                
        return f"The type of this animal is {self.type}, it's country is {self.country}."
    
obj = Animal("Dog","Japan")

print(obj.description())

print(obj.type)
print(obj.country)