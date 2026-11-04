def type_char(char):
    global curr_text
    undo_stk.append(curr_text)
    curr_text += char
    redo_stk.clear()
    print(curr_text)


def undo():
    global curr_text
    if undo_stk:
        redo_stk.append(curr_text)
        curr_text = undo_stk.pop()
        print(curr_text)
    else:
        print("NOTHING TO UNDO!")


def redo():
    global curr_text
    if redo_stk:
        undo_stk.append(curr_text)
        curr_text = redo_stk.pop()
        print(curr_text)
    else:
        print("NOTHING TO REDO!")


def show():
    global curr_text
    print("THE CURRENT TEXT IN EDITOR IS:", curr_text)


undo_stk = []
redo_stk = []
curr_text = ""

while True:
    print("\nUNDO AND REDO USING STACK")
    print("1. TYPE IN EDITOR")
    print("2. UNDO")
    print("3. REDO")
    print("4. SHOW CURRENT TEXT")
    print("5. EXIT")

    ch = int(input("ENTER YOUR CHOICE: "))

    if ch == 1:
        char = input("ENTER THE CHARACTER: ")
        type_char(char)
    elif ch == 2:
        undo()
    elif ch == 3:
        redo()
    elif ch == 4:
        show()
    elif ch == 5:
        print("THANK YOU!")
        break
    else:
        print("INVALID CHOICE!")
