from threading import Thread
from queue import Queue
import time


def producer(q: Queue[int]) -> None:
    for i in range(1, 6):
        print("Produced:", i)
        q.put(i)
        time.sleep(0.5)

    q.put(None)   # Stop signal


def consumer(q: Queue[int]) -> None:
    while True:
        item = q.get()

        if item is None:
            break

        print("Consumed:", item)
        q.task_done()


q = Queue()

p = Thread(target=producer, args=(q,))
c = Thread(target=consumer, args=(q,))

p.start()
c.start()

p.join()
c.join()

print("Processing completed")

