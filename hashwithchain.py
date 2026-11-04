Title : Implement a hash table of size 10 and use the division method as a hash
function. In case of a collision, use chaining. Implement the following operations:
• Insert(key): Insert key-value pairs into the hash table.
• Search(key): Search for the value associated with a given key.
• Delete(key): Delete a key-value pair from the hash table



def create_table(size):
    return [[] for i in range(size)]


def hash_function(key, size):
    return key % size


def insert(table, size, key):
    index = hash_function(key, size)
    table[index].append(key)
    print(f"Inserted key {key} at index {index}")


def search(table, size, key):
    index = hash_function(key, size)
    for item in table[index]:
        if item == key:
            print(f"Key {key} found at index {index}")
            return True
    print(f"Key {key} not found")
    return False


def delete(table, size, key):
    index = hash_function(key, size)
    for item in table[index]:
        if item == key:
            table[index].remove(item)
            print(f"Key {key} deleted from index {index}")
            return
    print(f"Key {key} not found, cannot delete")


def display(table, size):
    print("\nHash Table contents:")
    print("Index Value")
    for i in range(size):
        print(i, end="")
        if not table[i]:
            print(" --> -1", end="")
        else:
            for item in table[i]:
                print(f" --> {item}", end="")
        print()


size = 10
HashTable = create_table(size)

while True:
    print("\nHASHING WITH CHAINING")
    print("1. Insert")
    print("2. Search")
    print("3. Delete")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        key = int(input("Enter key: "))
        insert(HashTable, size, key)
    elif choice == 2:
        key = int(input("Enter key to search: "))
        search(HashTable, size, key)
    elif choice == 3:
        key = int(input("Enter key to delete: "))
        delete(HashTable, size, key)
    elif choice == 4:
        display(HashTable, size)
    elif choice == 5:
        print("Terminating...")
        break
    else:
        print("Invalid choice!")
