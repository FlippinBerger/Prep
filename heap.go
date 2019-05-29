package main

import (
	"errors"
	"fmt"
)

// Heap is a min heap implementation
type Heap struct {
	arr  []int
	size int
}

// Count returns the number of items in the heap
func (h *Heap) Count() int {
	return h.size
}

// Push adds a value to the heap
func (h *Heap) Push(val int) {
	h.arr = append(h.arr, val)
	h.heapifyUp(h.size)
	h.size++
}

func (h *Heap) heapifyUp(index int) {
	parent, err := parentIndex(index)

	if err != nil {
		return
	}

	if h.arr[index] < h.arr[parent] {
		h.arr[index], h.arr[parent] = h.arr[parent], h.arr[index]
		h.heapifyUp(parent)
	}
}

// Pop will return the smallest value from the heap
func (h *Heap) Pop() int {
	num := h.arr[0]

	//fmt.Println(h.arr)
	h.arr[0] = h.arr[h.size-1]

	h.heapifyDown(0)

	h.size--
	return num
}

func (h *Heap) heapifyDown(index int) {
	if h.hasLeftChild(index) {
		leftIndex, err := h.leftChild(index)
		if err != nil {
			return
		}
		min := leftIndex
		if h.size > leftIndex+1 && h.arr[leftIndex+1] < h.arr[leftIndex] {
			min = leftIndex + 1
		}

		h.arr[index], h.arr[min] = h.arr[min], h.arr[index]
		h.heapifyDown(min)
	}
}

func parentIndex(index int) (int, error) {
	if index == 0 {
		return -1, errors.New("No parent available")
	}

	return index / 2, nil
}

func (h *Heap) leftChild(index int) (int, error) {
	leftChild := index*2 + 1

	if leftChild >= h.size {
		return -1, errors.New("left child doesn't exist")
	}

	return leftChild, nil
}

func (h *Heap) rightChild(index int) (int, error) {
	rightChild := index*2 + 2

	if rightChild >= h.size {
		return -1, errors.New("right child doesn't exist")
	}

	return rightChild, nil
}

func (h *Heap) hasLeftChild(index int) bool {
	return h.size > index*2+1
}

// clear is a helper function to pop each value from the heap and print it
func (h *Heap) clear() {
	size := h.size
	for i := 0; i < size; i++ {
		fmt.Println(h.Pop())
	}
}

// test it
func main() {
	h := new(Heap)

	h.Push(10)
	h.Push(3)
	h.Push(16)
	h.Push(23)
	h.Push(2)
	h.Push(4)
	h.Push(12)

	h.clear()
}
