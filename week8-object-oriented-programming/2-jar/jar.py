class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        self._size += int(n)
        if self._size > self._capacity:
            raise ValueError("Size exceds capacity")

    def withdraw(self, n):
        self._size -= int(n)
        if self._size < 0:
            raise ValueError("Can't withdraw from 0")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity=12):
        if not capacity > 0:
            raise ValueError("Invalid capacity")
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size=0):
        if size > self._capacity:
            raise ValueError("Size is over than capacity")
        self._size = size
