""" March 09, 2017
@author: Phillip Le, philliple1337@gmail.com
"""


class Node:
    def __init__(self, next_node, value):
        self.next_node = next_node
        self.value = value


class LinkedList:
    def __init__(self):
        self.head = -1
        self.tail = -1

    def addFirst(self, value):
        if (self.head == -1):
            self.head = Node(-1, value)
        else:
            tmp = Node(self.head, value)
            self.head = tmp
        if (self.tail == -1):
            self.tail = self.head

    def addLast(self, value):
        if (self.head == -1):
            self.addFirst(-1, value)
        else:
            self.tail.next_node = Node(-1, value)
            self.tail = self.tail.next_node

    def show_all(self):
        val = ""
        if (self.head != -1) and (self.tail != -1):
            currentNode = self.head
            val += str(self.head.value) + " "
            while (currentNode.next_node != -1):
                currentNode = currentNode.next_node
                val += str(currentNode.value) + " "
        else:
            val = "empty"
        print(val)
        print(val[1])


list = LinkedList()
list.addFirst(12)
list.addFirst(3)


list.show_all()

