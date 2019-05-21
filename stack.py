from linked_list import LinkedList

class Stack:
    def __init__(self):
        self.ll = LinkedList()

    def length(self):
        return self.ll.count

    def push(self, val):
        self.ll.push(val)

    def pop(self):
        return self.ll.popFront().val


def main():
    print("Testing stack")

    s = Stack()
    s.push(10)
    print(f'The count is {s.length()}')
    print(f'The item is {s.pop()}')
    print(f'The length is {s.length()}')

    s.push(3)
    s.push(2)
    s.push(1)

    print(f'The length is {s.length()}')

    for i in range(3):
        print(s.pop())


if __name__ == '__main__':
    main()
