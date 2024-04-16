import numpy as np

class Deck:
    def __init__(self, capacity):
        self.capacity = capacity
        self.start = -1
        self.end = 0
        self.elements_number = 0
        self.values = np.empty(self.capacity, dtype = int)

    def __full_deck(self):
        return (self.start == 0 and self.end == self.capacity - 1) or (self.start == self.end + 1)
    
    def __empty_deck(self):
        return (self.start == -1 and self.end == 0)
    
    def insert_start(self, value):
        if self.__full_deck():
            print("Deck is full")
            return
        if self.start == -1:
            self.start = 0
            self.end = 0
        elif self.start == 0:
            self.start = self.capacity - 1
        else:
            self.start -= 1
        self.values[self.start] = value
        self.elements_number += 1

    def insert_end(self, value):
        if self.__full_deck():
            print("Deck is full")
            return
        
        if self.start == -1:
            self.start = 0
            self.end = 0
        elif self.end == self.capacity - 1:
            self.end = 0
        else:
            self.end += 1
        self.values[self.end] = value
        self.elements_number += 1

    def remove_start(self):
        if self.__empty_deck():
            print("Deck is empty")
            return
        if self.start == self.end:
            self.start = -1
            self.end = 0
        elif self.start == self.capacity - 1:
            self.start = 0
        else:
            self.start += 1
        self.elements_number -= 1
    
    def remove_end(self):
        if self.__empty_deck():
            print("Deck is empty")
            return
        if self.start == self.end:
            self.start = -1
            self.end = 0
        elif self.end == 0:
            self.end = self.capacity - 1
        else:
            self.end -= 1
        self.elements_number -= 1

    def get_start(self):
        if self.__empty_deck():
            print("Deck is empty")
            return
        return self.values[self.start]
    
    def get_end(self):
        if self.__empty_deck():
            print("Deck is empty")
            return
        return self.values[self.end]