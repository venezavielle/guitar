#!/usr/bin/env python3
class RingBuffer:
    def __init__(self, capacity: int):
        '''
        Create an empty ring buffer, with given max capacity
        '''

        self.MAX_CAP = capacity
        self._front = 0
        self._rear = 0
        self._size = 0
        self.buffer = [] * self.MAX_CAP

    def size(self) -> int:
        '''
        Return number of items currently in the buffer
        '''

        return self._size

    def is_empty(self) -> bool:
        '''
        Is the buffer empty (size equals zero)?
        '''

        return self._size == 0 #checks if size == 0 therefore empty
        
    def is_full(self) -> bool:
        '''
        Is the buffer full (size equals capacity)?
        '''

        return self._size == self.MAX_CAP  # checks if size has reached max cap therefore full

    def enqueue(self, x: float):
        '''
        Add item `x` to the end
        '''

        if self._size == self.MAX_CAP:
            raise RingBufferFull(Exception)
        self.buffer.append(x)
        self._size +=1


    def dequeue(self) -> float:
        '''
        Return and remove item from the front
        '''

        if self.is_empty():
            raise RingBufferEmpty(Exception)
        temp = self.buffer[0]
        self.buffer.pop(0)
        self._size -= 1
        return temp

    def peek(self) -> float:
        '''
        Return (but do not delete) item from the front
        '''

        if self._size == 0:
            raise RingBufferEmpty(Exception)
        return self.buffer[0]

class RingBufferFull(Exception):
    pass

class RingBufferEmpty(Exception):
    pass
