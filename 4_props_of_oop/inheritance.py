class Animal:
    def __init__(self, type, country):
        self.type = type
        self.country = country

    def description(self):                
        return f"The type of this animal is {self.type}, it's country is {self.country}."
    

class Siamese(Animal):     
    pass

class Vietnam(Animal):     
    def cat_desc(self):
        return "This is a Vietnam cat."

siamese = Siamese("cat","Siamese")
print(siamese.description())

vietnam = Vietnam("dog","Vietnam")
print(vietnam.description())
print(vietnam.cat_desc())
    