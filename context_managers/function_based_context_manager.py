# function_based_context_manager.py

from contextlib import contextmanager

from person import Person


@contextmanager
def greeting_context_manager():
    person = Person("Sergio")
    print(f"Hello {person.name}!")
    yield "Doing something..."
    print(f"Bye {person.name}!")


if __name__ == "__main__":
    with greeting_context_manager() as action:
        print(action)
