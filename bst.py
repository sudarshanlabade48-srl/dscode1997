Title : Implement various operations on a Binary Search Tree, such as

insertion, deletion, display and search.

def insert(root, key):
    if root is None:
        return {'key': key, 'left': None, 'right': None}

    if key < root['key']:
        root['left'] = insert(root['left'], key)
    elif key > root['key']:
        root['right'] = insert(root['right'], key)

    return root


def search(root, key):
    if root is None:
        return False

    if key == root['key']:
        return True
    elif key < root['key']:
        return search(root['left'], key)
    else:
        return search(root['right'], key)


def min_value_node(node):
    current = node
    while current['left'] is not None:
        current = current['left']
    return current


def delete(root, key):
    if root is None:
        return root, False

    if key < root['key']:
        root['left'], deleted = delete(root['left'], key)
        return root, deleted

    elif key > root['key']:
        root['right'], deleted = delete(root['right'], key)
        return root, deleted

    else:
        if root['left'] is None:
            return root['right'], True
        elif root['right'] is None:
            return root['left'], True

        temp = min_value_node(root['right'])
        root['key'] = temp['key']
        root['right'], deleted = delete(root['right'], temp['key'])
        return root, True


def inorder(root):
    if root:
        inorder(root['left'])
        print(root['key'], end=' ')
        inorder(root['right'])


root = None

n = int(input("ENTER NUMBER OF INITIAL KEYS TO INSERT: "))
print("ENTER THE KEYS:")

for i in range(n):
    key = int(input(f"ENTER THE KEY {i + 1}: "))
    root = insert(root, key)

while True:
    print("\nBINARY SEARCH TREE MENU")
    print("1. INSERT A KEY")
    print("2. SEARCH FOR A KEY")
    print("3. DELETE A KEY")
    print("4. DISPLAY BST")
    print("5. EXIT")

    choice = input("ENTER YOUR CHOICE (1-5): ")

    if choice == '1':
        key = int(input("ENTER KEY TO INSERT: "))
        root = insert(root, key)
        print(f"{key} INSERTED SUCCESSFULLY.")

    elif choice == '2':
        key = int(input("ENTER KEY TO SEARCH: "))
        if search(root, key):
            print(f"KEY {key} FOUND IN BST.")
        else:
            print(f"KEY {key} NOT FOUND IN BST.")

    elif choice == '3':
        key = int(input("ENTER KEY TO DELETE: "))
        root, deleted = delete(root, key)

        if deleted:
            print(f"KEY {key} DELETED SUCCESSFULLY.")
        else:
            print(f"KEY {key} NOT FOUND IN BST.")

    elif choice == '4':
        print("INORDER TRAVERSAL: ", end='')
        inorder(root)
        print()

    elif choice == '5':
        print("EXITING PROGRAM. GOODBYE!")
        break

    else:
        print("INVALID CHOICE! PLEASE ENTER A NUMBER BETWEEN 1 AND 5.")
