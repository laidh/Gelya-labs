import random

def generate_sequence(n, seq_type):
    if seq_type == "random":
        return [random.randint(1, 1000) for _ in range(n)]
    elif seq_type == "ascending":
        return list(range(1, n + 1))
    elif seq_type == "descending":
        return list(range(n, 0, -1))
    else:
        raise ValueError("Unknown sequence type")

def count_operations(arr, sort_func):
    comparisons = 0
    assignments = 0
    

    def custom_sort(arr):
        nonlocal comparisons, assignments
        for j in range(1, len(arr)):
            key = arr[j]
            assignments += 1  #
            
            i = j - 1
            while i >= 0 and arr[i] > key:
                comparisons += 1  
                arr[i + 1] = arr[i]
                assignments += 1  
                i -= 1
            if i >= 0:
                comparisons += 1  
            arr[i + 1] = key
            assignments += 1  
    
    custom_sort(arr)
    return comparisons, assignments
