
Title : Implement a real-time event processing system using a Queue data
structure. The systemshould support the following features:
• Add an Event: When a new event occurs, it should be added to the event queue.
• Process the Next Event: The system should process and remove the event that has
been in the queue the longest.
• Display Pending Events: Show all the events currently waiting to be processed.
• Cancel an Event: An event can be canceled if it has not been processed


def add(e):
    que.append(e)
    print(f"\nEVENT IS ADDED: {e}")
    print(que)


def process():
    if que:
        e = que.pop(0)
        print(f"\nEVENT IS PROCESSED: {e}")
        print(que)
    else:
        print("NO ELEMENTS TO PROCESS")


def display():
    if que:
        print("\nPENDING EVENTS")
        print(que)
    else:
        print("QUEUE IS EMPTY")


def cancel(e):
    if e in que:
        que.remove(e)
        print(f"\nEVENT IS CANCELED: {e}")
        print(que)
    else:
        print("EVENT NOT FOUND")


que = []

while True:
    print("\nEVENT MANAGEMENT")
    print("1. ADD AN EVENT")
    print("2. PROCESS THE NEXT EVENT")
    print("3. DISPLAY THE EVENTS")
    print("4. CANCEL AN EVENT")
    print("5. EXIT")

    ch = int(input("ENTER THE CHOICE (1-5): "))

    if ch == 1:
        e = int(input("ENTER THE EVENT: "))
        add(e)
    elif ch == 2:
        process()
    elif ch == 3:
        display()
    elif ch == 4:
        e = int(input("ENTER EVENT TO CANCEL: "))
        cancel(e)
    elif ch == 5:
        print("THANK YOU")
        break
    else:
        print("INVALID CHOICE")
