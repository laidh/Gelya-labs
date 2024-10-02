from random import*
from stack import Stack

def main():
    S = 16 * 5 + 50
    initial_stack = Stack()

    even_stack = Stack()
    odd_stack = Stack()

    for i in range(S):
        initial_stack.push(randint(1, 1000))

    while not initial_stack.isEmpty():
        num = initial_stack.pop()
        if num % 2 == 0:
            even_stack.push(num)
        else:
            odd_stack.push(num)

    print("Елементи парного стеку: ", end=" ")
    while not even_stack.isEmpty():
        print(even_stack.pop(), end=" ")

    print(f"\nЕлементи не парного стеку: ", end=" ")
    while not odd_stack.isEmpty():
        print(odd_stack.pop(), end=" ")

if __name__ == "__main__":
    main()

