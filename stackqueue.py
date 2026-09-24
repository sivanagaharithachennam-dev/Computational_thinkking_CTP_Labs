from dataclasses import dataclass, field
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass
class Stack(Generic[T]):
    items: list[T] = field(default_factory=list)

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()


@dataclass
class Queue(Generic[T]):
    items: list[T] = field(default_factory=list)

    def enqueue(self, item: T) -> None:
        self.items.append(item)

    def dequeue(self) -> T:
        return self.items.pop(0)


# Stack
stack = Stack[int]()

stack.push(10)
stack.push(20)
stack.push(30)

print("Stack:", stack.items)
print("Popped:", stack.pop())
print("Stack after pop:", stack.items)


# Queue
queue = Queue[str]()

queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")

print("Queue:", queue.items)
print("Dequeued:", queue.dequeue())
print("Queue after dequeue:", queue.items)