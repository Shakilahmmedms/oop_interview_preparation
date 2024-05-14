class Parent:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, I am {self.name}."

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def info(self):
        return f"My name is {self.name} and I am {self.age} years old."

# Creating an instance of the Child class
child = Child("Alice", 10)
print(child.greet())  
print(child.info())  
