# Linear Search and Binary Search

n = int(input("Enter number of accounts: "))

accounts = []

for i in range(n):
    x = int(input("Enter account ID: "))
    accounts.append(x)

key = int(input("Enter ID to search: "))

# Linear Search
linear_found = False

for i in range(n):
    if accounts[i] == key:
        linear_found = True
        break

if linear_found:
    print("Linear Search: Account ID Found")
else:
    print("Linear Search: Account ID Not Found")

# Binary Search
accounts.sort()

low = 0
high = n - 1
binary_found = False

while low <= high:
    mid = (low + high) // 2

    if accounts[mid] == key:
        binary_found = True
        break

    elif accounts[mid] < key:
        low = mid + 1

    else:
        high = mid - 1

if binary_found:
    print("Binary Search: Account ID Found")
else:
    print("Binary Search: Account ID Not Found")
