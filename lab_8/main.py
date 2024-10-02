import random
import time


def partition(A, p, r):
    comparisons = assignments = 0
    x = A[r]  
    i = p - 1
    for j in range(p, r):
        comparisons += 1
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]  
            assignments += 1
    A[i + 1], A[r] = A[r], A[i + 1]  
    assignments += 1
    return i + 1, comparisons, assignments

def quicksort(A, p, r):
    comparisons = assignments = 0
    if p < r:
        q, comp, assign = partition(A, p, r)
        comparisons += comp
        assignments += assign
        comp, assign = quicksort(A, p, q - 1)
        comparisons += comp
        assignments += assign
        comp, assign = quicksort(A, q + 1, r)
        comparisons += comp
        assignments += assign
    return comparisons, assignments

def generate_sequence(n, sequence_type='random'):
    if sequence_type == 'random':
        return [random.randint(1, 10000) for _ in range(n)]
    elif sequence_type == 'ascending':
        return list(range(1, n + 1))
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

            comparisons, assignments = quicksort(A, 0, n - 1)

            elapsed_time = time.time() - start_time

            print(f"{sequence_type:<15} {n:<20} {elapsed_time:<20.6f} {comparisons:<15} {assignments:<15}")

if __name__ == "__main__":
    main()
