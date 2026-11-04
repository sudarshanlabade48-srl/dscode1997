Title : Design and implement a hash table of fixed size. Use the division method for
the hash function and resolve collisions using linear probing. Allow the user to
perform the following
operations:
• Insert a key
• Search for a key
• Delete a key
• Display the table



def hash_function(k, size):
    return k % size


def insert(k):
    size = len(hash_table)
    index = hash_function(k, size)

    for _ in range(size):
        if hash_table[index] == -1:
            hash_table[index] = k
            print("KEY INSERTED AT INDEX", index)
            return
        elif hash_table[index] == k:
            print("KEY ALREADY EXISTS AT INDEX", index)
            return
        else:
            index = (index + 1) % size

    print("HASH TABLE IS FULL")


def search(k):
    size = len(hash_table)
    index = hash_function(k, size)

    for _ in range(size):
        if hash_table[index] == -1:
            break
        elif hash_table[index] == k:
            print("KEY FOUND AT INDEX", index)
            return
        else:
            index = (index + 1) % size

    print("KEY NOT FOUND")


def delete(k):
    size = len(hash_table)
    index = hash_function(k, size)

    for _ in range(size):
        if hash_table[index] == -1:
            break
        elif hash_table[index] == k:
            hash_table[index] = -1
            print("KEY DELETED FROM INDEX", index)
            return
        else:
            index = (index + 1) % size

    print("KEY NOT FOUND, CANNOT DELETE")


def display():
    print("\nHASH TABLE:")
    for i in range(len(hash_table)):
        print(f"INDEX {i}: {hash_table[i]}")
    print()


size = int(input("ENTER SIZE OF HASH TABLE: "))

if size <= 0:
    print("HASH TABLE SIZE MUST BE GREATER THAN ZERO")
else:
    hash_table = [-1] * size

    while True:
        print("\nHASHING USING LINEAR PROBING")
        print("1. INSERT")
        print("2. SEARCH")
        print("3. DELETE")
        print("4. DISPLAY")
        print("5. EXIT")

        choice = input("ENTER YOUR CHOICE: ")

        if choice == "1":
            k = int(input("ENTER KEY TO INSERT: "))
            insert(k)
        elif choice == "2":
            k = int(input("ENTER KEY TO SEARCH: "))
            search(k)
        elif choice == "3":
            k = int(input("ENTER KEY TO DELETE: "))
            delete(k)
        elif choice == "4":
            display()
        elif choice == "5":
            print("THANK YOU!")
            break
        else:
            print("INVALID CHOICE! PLEASE ENTER 1-5")
