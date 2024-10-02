from binaryTree import BinaryTree

def create_phone_directory():
    phone_directory = BinaryTree()

    phone_directory.insert("Іванов", "123-456-789")
    phone_directory.insert("Петров", "987-654-321")
    phone_directory.insert("Сидоров", "555-555-555")
    phone_directory.insert("Ковальчук", "111-111-111")
    phone_directory.insert("Ткаченко", "222-222-222")

    return phone_directory

def main():
    directory = create_phone_directory()

    print("Телефонний довідник (ін-ордер обхід):")
    for key, value in directory.inorder_traversal():
        print(f"{key}: {value}")

    search_key = "Петров"
    print(f"\nПошук номера телефону для {search_key}:")
    result = directory.search(search_key)
    if result:
        print(f"Знайдено: {search_key} - {result.value}")
    else:
        print(f"{search_key} не знайдено")

    delete_key = "Сидоров"
    print(f"\nВидалення {delete_key} з довідника:")
    directory.delete(delete_key)

    print("Телефонний довідник після видалення:")
    for key, value in directory.inorder_traversal():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()