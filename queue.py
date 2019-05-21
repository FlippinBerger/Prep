from linked_list import LinkedList

class Queue:
    def __init__(self):
        self.ll = LinkedList()

    def length(self):
        return self.ll.length()

    def push(self, val):
        self.ll.append(val)

    def pop(self):
        return self.ll.popFront().val

def main():
    print("Testing queue")

    q = Queue()
    q.push(10)
    print(f'The count is {q.length()}')
    print(f'The item is {q.pop()}')
    print(f'The length is {q.length()}')

    q.push(3)
    q.push(2)
    q.push(1)

    print(f'The length is {q.length()}')

    for i in range(3):
        print(q.pop())


if __name__ == '__main__':
    main()
