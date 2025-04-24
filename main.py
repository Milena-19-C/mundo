from collections.abc import async_generator


class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age
if__name__ == '__main__':
    person = Person("John", 36)
    print(person.name)
    print(person.age)