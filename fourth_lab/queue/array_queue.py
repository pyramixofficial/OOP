class EmptyQueueException(Exception):
    """Exception raised when performing an operation on an empty queue."""
    pass

class ArrayQueue:
    """Implements a queue data structure using a dynamically resizing array."""

    def __init__(self, capacity):
        """
        Initializes the ArrayQueue with a given capacity.

        Args:
            capacity: The initial capacity of the queue.
        """
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0

    def enqueue(self, element):
        """
        Adds an element to the rear of the queue.

        Args:
            element: The element to be added to the queue.
        """
        if self.size == self.capacity:
            self._resize_array()
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = element
        self.size += 1

    def dequeue(self):
        """
        Removes and returns the front element of the queue.

        Returns:
            The element at the front of the queue.

        Raises:
            EmptyQueueException: If the queue is empty.
        """
        if self.is_empty():
            raise EmptyQueueException("Queue is empty")
        removed_element = self.array[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return removed_element

    def peek(self):
        """
        Returns the front element of the queue without removing it.

        Returns:
            The element at the front of the queue.

        Raises:
            EmptyQueueException: If the queue is empty.
        """
        if self.is_empty():
            raise EmptyQueueException("Queue is empty")
        return self.array[self.front]

