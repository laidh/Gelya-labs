import random
from queue import Queue

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def main():
    S = 16 * 5 + 50
    queue = Queue(S)

    for i in range(S):
        queue.enqueue(random.randint(1, 1000))

    while not queue.isEmpty():
        num = queue.dequeue()
        if isPrime(num):
            print(num, end=" ")

if __name__ == "__main__":
    main()