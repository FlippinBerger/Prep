#implementation of a min heap
class Heap:
    def __init__(self):
        self.l = []

    def isEmpty(self):
        return len(self.l) == 0

    #gets the parent index for a given index in the heap's underlying array
    def parentIndex(self, index):
        return index // 2

    def leftIndex(self, index):
        return index * 2 + 1

    def rightIndex(self, index):
        return index * 2 + 2

    def hasLeftChild(self, index):
        return len(self.l) > 2 * index + 1

    def push(self, val):
        self.l.append(val)
        self.heapifyUp(len(self.l) - 1)

    def heapifyUp(self, index):
        parent = self.parentIndex(index)

        # swap them because the heap property isn't satisfied
        if self.l[index] < self.l[parent]:
            self.l[index], self.l[parent] = self.l[parent], self.l[index]
            self.heapifyUp(parent)

    def pop(self):
        if (len(self.l) == 0):
            return

        min = self.l[0]

        #replace the root with the last element in the array
        self.l[0] = self.l[len(self.l) - 1]
        self.l.pop()
        self.heapifyDown(0)
        return min

    def heapifyDown(self, index):
        if (self.hasLeftChild(index)):
            leftIndex = self.leftIndex(index)
            min = leftIndex
            if len(self.l) > leftIndex + 1 and self.l[leftIndex] > self.l[leftIndex+1]:
                min = leftIndex + 1

            self.l[index], self.l[min] = self.l[min], self.l[index]


def main():
    print("Testing heap")

    h = Heap()
    h.push(1)
    print(f'{h.pop()}')

    h.push(2)
    h.push(8)
    h.push(7)
    h.push(15)
    h.push(9)
    h.push(10)

    while not h.isEmpty():
        print(h.pop())

if __name__ == '__main__':
    main()
