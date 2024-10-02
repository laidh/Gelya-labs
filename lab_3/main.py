from random import*
from hashtable import HashTable

def main():
    N = 16 * 5 + 50
    S = int(N*0.75)

    hash_table = HashTable(S)

    print(f"Заповнення хеш таблиці з {S} елементів: ")
    for i in range(N):
        number = randint(0,1000)
        hash_table.insert(i,number)

    print("Таблиця до видалення парних чисел")
    hash_table.printer()

    del_keys = [key for key, value in hash_table.table.items() if value % 2 == 0]
    for key in del_keys:
        hash_table.delete(key)

    print("Таблиця після видалення парних чисел")
    hash_table.printer()


if __name__ == "__main__":
    main()