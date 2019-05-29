package main

import (
	"fmt"
)

type Node struct {
	value int
	next  *Node
}

type LinkedList struct {
	head  *Node
	count int
}

func (list *LinkedList) Count() int {
	return list.count
}

func (l *LinkedList) Append(val int) {
	newNode := Node{value: val}

	if l.count == 0 {
		l.head = &newNode
	} else {
		node := l.head
		for node.next != nil {
			node = node.next
		}

		node.next = &newNode
	}

	l.count++
}

func (l *LinkedList) Remove(val int) {
	node := l.head
	var prev *Node

	for node.value != val {
		prev = node
		node = node.next
	}

	if node.value == val {
		prev.next = node.next
		node = node.next
		l.count--
	}
}

func (l *LinkedList) Traverse() {
	node := l.head

	for node != nil {
		fmt.Println(node.value)
		node = node.next
	}
}

// simple testing down here
func main() {
	l := new(LinkedList)
	l.Append(1)
	l.Append(2)
	l.Append(3)

	l.Traverse()

	l.Remove(3)
	l.Traverse()

	l.Append(4)
	l.Traverse()

	l.Remove(2)
	l.Traverse()
}
