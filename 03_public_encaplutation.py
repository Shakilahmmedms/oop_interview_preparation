class Person:
    def __init__(self, name, age) -> None:
        self.__name = name
        self.__age = age

    def showDetail(self):
        print(f'My name is ',self.__name, 'and my age is ',self.__age)

p1 = Person('Shakil',22)
p1.showDetail()