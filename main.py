from queue import Queue
from stack import Stack

if (__name__ == "__main__"):
    # Queue test
    new_queue = Queue()

    new_queue.enqueue(45)
    new_queue.enqueue(508)
    new_queue.enqueue(123)

    print(new_queue)

    print(f"Queue dequeued element: {new_queue.dequeue()}")
    print(f"Queue dequeued element: {new_queue.dequeue()}")

    print(new_queue)

    print(f"Queue peek element: {new_queue.peek()}")

    print(new_queue.is_null())

    print(f"Queue dequeued element: {new_queue.dequeue()}")

    print(new_queue.dequeue())

    print(new_queue)

    print("")

    # Stack test
    new_stack = Stack()

    new_stack.push(2)
    new_stack.push(56)
    new_stack.push(89)

    print(new_stack)

    print(f"Stack popped element: {new_stack.pop()}")
    print(f"Stack popped element: {new_stack.pop()}")
    print(f"Stack popped element: {new_stack.pop()}")

    print(new_stack)

    print(new_stack.is_empty())

    print(new_stack.pop())
