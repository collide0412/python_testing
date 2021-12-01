class Dog:
    def description(self):
        print("This is a dog")

class Cat:
    def description(self):
        print("This is a cat")
    
cat = Cat()
dog = Dog()
for animal in (cat,dog):
 animal.description()