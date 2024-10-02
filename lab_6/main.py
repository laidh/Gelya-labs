import random
import time


def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    left = A[p:q + 1]  
    right = A[q + 1:r + 1]  

    i = j = 0
    k = p
    comparisons = 0
    assignments = 0


    while i < n1 and j < n2:
        comparisons += 1
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        assignments += 1
        k += 1


    while i < n1:
        A[k] = left[i]
        i += 1
        k += 1
        assignments += 1


    while j < n2:
        A[k] = right[j]
        j += 1
        k += 1
        assignments += 1

    return comparisons, assignments


def merge_sort(A, p, r):
    comparisons = assignments = 0
    if p < r:
        q = (p + r) // 2
        comp_left, assign_left = merge_sort(A, p, q)
        comp_right, assign_right = merge_sort(A, q + 1, r)
        comp_merge, assign_merge = merge(A, p, q, r)

        comparisons = comp_left + comp_right + comp_merge
        assignments = assign_left + assign_right + assign_merge

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


    print(f"{'Тип послідовності':<15} {'Кількість елементів':<20} {'Час (с)':<10} {'Порівнянь':<15} {'Присвоєнь':<15}")
    print("="*75)


    for sequence_type in sequence_types:
        for n in num_elements:
            A = generate_sequence(n, sequence_type)
            start_time = time.time()

            comparisons, assignments = merge_sort(A, 0, len(A) - 1)

            elapsed_time = time.time() - start_time

            print(f"{sequence_type:<15} {n:<20} {elapsed_time:<10.6f} {comparisons:<15} {assignments:<15}")

if __name__ == "__main__":
    main()
