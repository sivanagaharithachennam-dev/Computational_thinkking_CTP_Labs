import time
import sys


def list_processing(n):
    return [x * x for x in range(n)]


def generator_processing(n):
    return (x * x for x in range(n))


n = 1_000_000


# List processing
start = time.time()

data = list_processing(n)

list_time = time.time() - start
list_memory = sys.getsizeof(data)


# Generator processing
start = time.time()

generator = generator_processing(n)

for value in generator:
    pass

generator_time = time.time() - start
generator_memory = sys.getsizeof(generator)


print("List Time:", list_time)
print("Generator Time:", generator_time)

print("List Memory:", list_memory, "bytes")
print("Generator Memory:", generator_memory, "bytes")