
array = []
def queue_implement():
    size = int(input("Enter the size of the queue : "))
    while True:
        print("1: ENQUEUE\n2: DEQUEUE\n0: EXIT")
        op = int(input("Enter the operation : "))
        if op == 1:
            print("ENQUEUE OPERATION")
            if len(array) >= size:
                print("ERROR: Size of the queue exceeded")
                break
            else:
                element = int(input("Enter the element to enqueue: "))
                array.append(element)
        elif op == 2:
            print("DEQUEUE OPERATION")
            if len(array) == 0:
                print("QUEUE is empty")
                break
            else:
                dequeue = array.pop(0)
                print(array)
                print("Removed element is : ",dequeue)
        elif op == 0:
            print("EXITING")
            break
        else:
            print("INVALID OPERATION SELECTED\nPLEASE SELECT A VALID OPERATION")
            break
queue_implement()