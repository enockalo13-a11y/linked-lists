"""
Author: Enock Alo (Student ID: 226054861)

Data Structures and Algorithms - Lecture 7: Linear & Linked Lists
Python implementation of the pseudocode algorithms in the slides.

Three implementations of the List ADT:
  1. ArrayList          (slides 16-19)  - 0-based Index, as in the slides
  2. SinglyLinkedList   (slides 21-29)  - 1-based Position, as in the slides
  3. DoublyLinkedList   (slides 30-35)  - 1-based Position, as in the slides

Operations (List ADT, slide 15):
  is_empty, list_size, get, index_of / position_of, delete, insert, output
"""


# ---------------------------------------------------------------------------
# 1. Array implementation
# ---------------------------------------------------------------------------
class ArrayList:
    def __init__(self, array_length=10):
        self.A = [None] * array_length      # fixed-size array
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def list_size(self):
        # Slide version counts the non-NULL cells
        size = 0
        for i in range(len(self.A)):
            if self.A[i] is not None:
                size += 1
        return size

    def get(self, index):
        if 0 <= index < len(self.A) and self.A[index] is not None:
            return self.A[index]
        print("Wrong Index")
        return None

    def index_of(self, x):
        for i in range(self.size):
            if self.A[i] == x:
                return i
        return -1                           # not found

    def delete(self, index):
        if not (0 <= index < self.size):
            print("Wrong Index")
            return
        if index == self.size - 1:
            self.A[index] = None
        else:
            for i in range(index, self.size - 1):   # shift left
                self.A[i] = self.A[i + 1]
            self.A[self.size - 1] = None
        self.size -= 1

    def insert(self, index, x):
        if self.size == len(self.A):
            print("List is full")
            return
        if not (0 <= index <= self.size):
            print("Wrong Index")
            return
        if index == self.size:
            self.A[index] = x
        else:
            for i in range(self.size - 1, index - 1, -1):   # shift right
                self.A[i + 1] = self.A[i]
            self.A[index] = x
        self.size += 1

    def output(self):
        return [self.A[i] for i in range(self.size)]


# ---------------------------------------------------------------------------
# 2. Singly linked list
# ---------------------------------------------------------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def list_size(self):
        return self.size

    def get(self, position):
        if not (1 <= position <= self.size):
            print("Wrong Position")
            return None
        h = self.head
        count = 1
        while count < position:
            h = h.next
            count += 1
        return h.data

    def position_of(self, x):
        h = self.head
        count = 1
        while count <= self.size:
            if h.data == x:
                return count
            h = h.next
            count += 1
        return -1                           # not found

    def insert(self, position, x):
        if not (1 <= position <= self.size + 1):
            print("Wrong Position")
            return
        n = Node(x)
        if position == 1:                   # at the beginning
            n.next = self.head
            self.head = n
        elif position == self.size + 1:     # at the end
            h = self.head
            while h.next is not None:
                h = h.next
            h.next = n
        else:                               # in the middle
            count = 1
            h = self.head
            while count < position - 1:
                h = h.next
                count += 1
            n.next = h.next
            h.next = n
        self.size += 1

    def delete(self, position):
        if not (1 <= position <= self.size):
            print("Wrong Position")
            return
        if position == 1:
            self.head = self.head.next
        elif position == self.size:         # last node
            h = self.head
            count = 1
            while count < position - 1:
                h = h.next
                count += 1
            h.next = None
        else:                               # middle node
            h = self.head
            count = 1
            while count < position - 1:
                h = h.next
                count += 1
            h.next = h.next.next
        self.size -= 1

    def output(self):
        result = []
        h = self.head
        while h is not None:
            result.append(h.data)
            h = h.next
        return result


# ---------------------------------------------------------------------------
# 3. Doubly linked list
# ---------------------------------------------------------------------------
class DNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def list_size(self):
        return self.size

    def get(self, position):
        if not (1 <= position <= self.size):
            print("Wrong Position")
            return None
        h = self.head
        count = 1
        while count < position:
            h = h.next
            count += 1
        return h.data

    def position_of(self, x):
        h = self.head
        count = 1
        while count <= self.size:
            if h.data == x:
                return count
            h = h.next
            count += 1
        return -1

    def insert(self, position, x):
        if not (1 <= position <= self.size + 1):
            print("Wrong Position")
            return
        n = DNode(x)
        if self.size == 0:                  # empty list: Head = Tail = new node
            self.head = self.tail = n
        elif position == 1:
            n.next = self.head
            self.head.prev = n
            self.head = n
        elif position == self.size + 1:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n
        else:
            count = 1
            h = self.head
            while count < position - 1:
                h = h.next
                count += 1
            n.next = h.next
            n.prev = h
            h.next.prev = n
            h.next = n
        self.size += 1

    def delete(self, position):
        if not (1 <= position <= self.size):
            print("Wrong Position")
            return
        if self.size == 1:                  # only node: list becomes empty
            self.head = self.tail = None
        elif position == 1:
            self.head = self.head.next
            self.head.prev = None
        elif position == self.size:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            h = self.head
            count = 1
            while count < position - 1:
                h = h.next
                count += 1
            h.next = h.next.next
            h.next.prev = h
        self.size -= 1

    def output(self):
        result = []
        h = self.head
        while h is not None:
            result.append(h.data)
            h = h.next
        return result

    def output_reverse(self):
        """Bonus: walk back from the Tail using the prev pointers."""
        result = []
        t = self.tail
        while t is not None:
            result.append(t.data)
            t = t.prev
        return result


# ---------------------------------------------------------------------------
# Demo / self-test
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=== Array List (0-based index) ===")
    a = ArrayList(10)
    for i, v in enumerate([10, 20, 30, 40, 50]):
        a.insert(i, v)
    a.insert(0, 5)                          # insert at front
    a.insert(3, 25)                         # insert in the middle
    print("After inserts :", a.output(), "size =", a.list_size())
    print("get(2)        :", a.get(2))
    print("index_of(40)  :", a.index_of(40))
    a.delete(0)
    a.delete(a.size - 1)
    print("After deletes :", a.output(), "is_empty =", a.is_empty())

    print("\n=== Singly Linked List (1-based position) ===")
    s = SinglyLinkedList()
    s.insert(1, "B")                        # beginning
    s.insert(1, "A")                        # beginning
    s.insert(3, "D")                        # end
    s.insert(3, "C")                        # middle
    print("After inserts :", s.output(), "size =", s.list_size())
    print("get(3)        :", s.get(3))
    print("position_of('D'):", s.position_of("D"))
    s.delete(1)                             # first
    s.delete(s.size)                        # last
    print("After deletes :", s.output())

    print("\n=== Doubly Linked List (1-based position) ===")
    d = DoublyLinkedList()
    d.insert(1, 2)
    d.insert(1, 1)
    d.insert(3, 4)
    d.insert(3, 3)
    print("After inserts :", d.output(), "reverse =", d.output_reverse())
    print("get(2)        :", d.get(2))
    print("position_of(4):", d.position_of(4))
    d.delete(1)
    d.delete(d.size)
    print("After deletes :", d.output(), "reverse =", d.output_reverse())
    d.delete(1)
    d.delete(1)
    print("Emptied       :", d.output(), "is_empty =", d.is_empty())
