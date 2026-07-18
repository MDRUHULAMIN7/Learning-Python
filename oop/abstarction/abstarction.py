from abc import ABC, abstractmethod

class Animal(ABC):           # Abstract Class

    @abstractmethod
    def make_sound(self):    # Abstract Method
        pass


class Dog(Animal):

    def make_sound(self):
        print("Dog says Woof!")


d = Dog()
d.make_sound()