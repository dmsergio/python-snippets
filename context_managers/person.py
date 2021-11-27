# person.py


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<{self.__class__.__name__}>({self.name})"

    def __str__(self):
        return self.__repr__()
