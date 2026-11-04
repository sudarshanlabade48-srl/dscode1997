
def average(l):
    total = sum(l)
    avg = total / len(l)
    print("\nTotal books borrowed by all members:", total)
    print("Average number of books borrowed: {:.2f}".format(avg))


def Maximum(l):
    return max(l)


def Minimum(l):
    non_zero = [x for x in l if x > 0]
    if not non_zero:
        return 0
    return min(non_zero)


def count(l):
    return l.count(0)


def maxFrequency(l):
    frequencies = {}
    for ele in l:
        frequencies[ele] = frequencies.get(ele, 0) + 1
    member = max(frequencies, key=frequencies.get)
    return member, frequencies[member]


lib = []
print("LIBRARY BORROWING RECORDS")
n = int(input("Enter total number of members in library: "))

for i in range(n):
    m = int(input("Enter books borrowed by Member " + str(i + 1) + ": "))
    lib.append(m)

while True:
    print("\nMENU")
    print("1. Average number of books borrowed")
    print("2. Highest and lowest books borrowed")
    print("3. Count members who borrowed no books")
    print("4. Display most frequent borrowing count")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        average(lib)
    elif choice == 2:
        print("Highest books borrowed by a member:", Maximum(lib))
        print("Lowest non-zero books borrowed by a member:", Minimum(lib))
    elif choice == 3:
        print("Members who borrowed no books:", count(lib))
    elif choice == 4:
        m, frequency = maxFrequency(lib)
        print("Most frequent borrowing count:", m)
        print("Frequency:", frequency)
    elif choice == 5:
        print("Successfully terminated")
        break
    else:
        print("Wrong choice")
