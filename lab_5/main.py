import time
from sort import sort
from utils import generate_sequence, count_operations

def main():
    n_values = [10, 100, 1000, 5000, 10000]
    
    sequence_types = ["random", "ascending", "descending"]
    
    print(f"{'Тип послідовності':<15} {'n':<10} {'Час (с)':<15} {'Порівнянь':<15} {'Присвоювань':<15}")
    
    for n in n_values:
        for seq_type in sequence_types:
            sequence = generate_sequence(n, seq_type)
            sequence_copy = sequence.copy()  

            start_time = time.time()
            comparisons, assignments = count_operations(sequence_copy, sort)
            end_time = time.time()

            time_taken = end_time - start_time
            print(f"{seq_type:<15} {n:<10} {time_taken:<15.6f} {comparisons:<15} {assignments:<15}")

if __name__ == "__main__":
    main()
