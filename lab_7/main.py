import random
import time

def max_heapify(A, n, i):
    comparisons = 0
    assignments = 0
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2


    if left < n and A[left] > A[largest]:
        largest = left
        comparisons += 1


    if right < n and A[right] > A[largest]:
        largest = right
        comparisons += 1

    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        assignments += 1
        comp, assign = max_heapify(A, n, largest)
        comparisons += comp
        assignments += assign

    return comparisons, assignments


def build_max_heap(A, n):
    comparisons = assignments = 0
    for i in range(n // 2 - 1, -1, -1):
        comp, assign = max_heapify(A, n, i)
        comparisons += comp
        assignments += assign
    return comparisons, assignments


def heap_sort(A):
    n = len(A)
    comparisons = assignments = 0


    comp, assign = build_max_heap(A, n)
    comparisons += comp
    assignments += assign

    for i in range(n - 1, 0, -1):
        A[i], A[0] = A[0], A[i]  
        assignments += 1
        comp, assign = max_heapify(A, i, 0)
        comparisons += comp
        assignments += assign

    return comparisons, assignments


def generate_sequence(n, sequence_type='random'):
    if sequence_type == 'random':
        return [random.randint(1, 10000) for _ in range(n)]
    elif sequence_type == 'ascending':
        return list(range(1, n+1))
    elif sequence_type == 'descending':
        return list(range(n, 0, -1))


def main():
    num_elements = [10, 100, 1000, 5000, 10000]
    sequence_types = ['random', 'ascending', 'descending']

    print(f"{'Тип послідовності':<15} {'Кількість елементів':<20} {'Час сортування (с)':<20} {'Порівняння':<15} {'Присвоєння':<15}")
    print("-" * 85)

    for sequence_type in sequence_types:
        for n in num_elements:
            A = generate_sequence(n, sequence_type)
            start_time = time.time()

            comparisons, assignments = heap_sort(A)

            elapsed_time = time.time() - start_time

            print(f"{sequence_type:<15} {n:<20} {elapsed_time:<20.6f} {comparisons:<15} {assignments:<15}")

if __name__ == "__main__":
    main()
