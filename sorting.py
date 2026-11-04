
def Selection_Sort(c):
    for i in range(len(c)):
        min_idx = i
        for j in range(i + 1, len(c)):
            if c[min_idx] > c[j]:
                min_idx = j
        c[i], c[min_idx] = c[min_idx], c[i]

    print("SALARY AFTER SELECTION SORT:")
    for salary in c:
        print(salary)


def Bubble_Sort(c):
    n = len(c)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if c[j] > c[j + 1]:
                c[j], c[j + 1] = c[j + 1], c[j]

    print("SALARY AFTER BUBBLE SORT:")
    for salary in c:
        print(salary)


def top_five_salary(c):
    print("TOP FIVE HIGHEST SALARIES:")
    count = 0
    for i in range(len(c) - 1, -1, -1):
        print(c[i])
        count += 1
        if count == 5:
            break


com = []

n = int(input("ENTER TOTAL NUMBER OF EMPLOYEES: "))

for i in range(n):
    ele = float(input("Enter salary of employee " + str(i + 1) + ": "))
    com.append(ele)

print("SALARIES OF EMPLOYEES:")
print(com)

while True:
    print("\nMENU")
    print("1. SELECTION SORT")
    print("2. BUBBLE SORT")
    print("3. TOP FIVE USING SELECTION SORT")
    print("4. TOP FIVE USING BUBBLE SORT")
    print("5. EXIT")

    ch = int(input("ENTER YOUR CHOICE (1-5): "))

    if ch == 1:
        Selection_Sort(com)
    elif ch == 2:
        Bubble_Sort(com)
    elif ch == 3:
        Selection_Sort(com)
        top_five_salary(com)
    elif ch == 4:
        Bubble_Sort(com)
        top_five_salary(com)
    elif ch == 5:
        print("TERMINATED")
        break
    else:
        print("INVALID CHOICE")
