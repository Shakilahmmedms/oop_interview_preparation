class Person: #this is a class in python
    def __init__(self, name,age) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f'My name is {self.name} and my age {self.age}'
    

p1 = Person('Shakil',22) # this is an object in python 

print(p1)