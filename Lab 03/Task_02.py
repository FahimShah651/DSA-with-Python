class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}\nAge: {self.age}")
        
person = Person("John", 25)
person.display_info()
