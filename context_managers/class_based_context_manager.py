# class_based_context_manager.py


class GreetingContextManager:
    def __init__(self, person):
        self.person = person

    def __enter__(self):
        print(f"{self.person} has entered on __enter__ method")
        print(f"Hello {self.person.name}!")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{self.person} has entered on __exit__ method")
        print(f"Bye {self.person.name}")


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<{self.__class__.__name__}>({self.name})"

    def __str__(self):
        return self.__repr__()


if __name__ == "__main__":
    person = Person("Sergio")
    with GreetingContextManager(person):
        ...
