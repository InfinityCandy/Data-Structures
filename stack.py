from typing import Any


class Stack:

    def __init__(self):
        self.stack = []
        self.counter = 0

    def __str__(self):
        string_reperesentation = ""

        if (self.counter == 0):
            string_reperesentation = "Empty Stack"

        else:
            for index, element in enumerate(self.stack):
                if (index == self.counter - 1):
                    string_reperesentation = string_reperesentation + \
                        str(element)

                else:
                    string_reperesentation = string_reperesentation + \
                        str(element) + "<-"

        return string_reperesentation

    def push(self, element) -> None:
        self.stack.append(element)
        self.counter += 1

    def pop(self) -> Any:
        if (self.is_empty()):
            return "Can't perform operation on empty Stack"

        else:
            self.counter -= 1

            return self.stack.pop()

    def is_empty(self) -> bool:
        if (self.counter == 0):
            return True
        else:
            return False
