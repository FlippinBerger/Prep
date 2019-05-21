class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# head is a Node
class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def isEmpty(self):
        return self.head == None

    def length(self):
        return self.count

    def append(self, val):
        newNode = Node(val)

        if (self.isEmpty()):
            self.head = newNode
        else:
            node = self.head
            while node.next != None:
                node = node.next

            node.next = newNode
        self.count += 1

    def push(self, val):
        newNode = Node(val)

        if (not self.isEmpty()):
            newNode.next, self.head = self.head, newNode
        else:
            self.head = newNode
        self.count += 1

    def popFront(self):
        if (not self.isEmpty()):
            node = self.head
            self.head = self.head.next
            self.count -= 1
            return node

    # deletes first occurrence of val in the linked list
    # returns true if it was deleted properly
    def delete(self, val):
        if self.head.val == val:
            self.head = self.head.next
            self.count -= 1
            return True
        node = self.head
        while node.next != None and node.next.val != val:
            node = node.next

        # we reached the end of the list and haven't found the value
        if node.next == None:
            return False

        node.next = node.next.next
        self.count -= 1
        return True

    def find(self, val):
        node = self.head
        while node.val != val and node.next != None:
            node = node.next

        return node if node.val == val else False






