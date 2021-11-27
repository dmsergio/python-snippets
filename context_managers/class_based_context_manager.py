# class_based_context_manager.py

from person import Person


class GreetingContextManager:
    def __init__(self, person):
        self.person = person

    def __enter__(self):
        print(f"{self.person} has entered on {self.__enter__.__name__} method")
        print(f"Hello {self.person.name}!")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"{self.person} has entered on {self.__exit__.__name__} method")
        print(f"Bye {self.person.name}")


if __name__ == "__main__":
    person = Person("Sergio")
    with GreetingContextManager(person):
        ...
