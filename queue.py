from typing import Any


class Queue:
    def __init__(self):
        self.queue = []
        self.counter = 0

    def __str__(self):
        string_representation = ""

        if (self.counter == 0):
            string_representation = "Empty Queue"

        else:
            for index, element in enumerate(self.queue):
                if (index == self.counter - 1):
                    string_representation = string_representation + \
                        str(element)
                else:
                    string_representation = string_representation + \
                        str(element) + "<-"

        return string_representation

    def enqueue(self, element: Any) -> None:
        self.queue.append(element)
        self.counter += 1

    def dequeue(self) -> Any:
        if (self.is_null()):
            return "Can't perform operation on empty queue"

        else:
            dequeue_val = self.queue[0]

            new_queue = self.queue[1:]
            self.queue = new_queue

            self.counter -= 1

            return dequeue_val

    def peek(self) -> Any:
        return self.queue[0]

    def size(self):
        return self.counter

    def is_null(self) -> bool:
        if (self.counter == 0):
            return True
        else:
            return False
