import numpy as np

class CircularPriorityList:
    
    def __init__(self, capacity):
        self.capacity = capacity
        self.start = -1
        self.end = 0
        self.elements_number = 0
        self.values = np.empty(self.capacity, dtype=int)
    
    def __empty_list(self):
        return self.elements_number == 0
    
    def __full_list(self):
        return self.elements_number == self.capacity
    
    def queue(self, value):
        if self.__full_list():
            return print("A fila está cheia!!!")
        
        x = self.elements_number - 1
        while x >= 0:
            if value > self.values[x]:
                self.values[x + 1] = self.values[x]
            else:
                break
            x -= 1
        self.values[x + 1] = value
        self.elements_number += 1
            
        
    def dequeue(self):
        if self.__empty_list():
            return print("A fila está vazia!!!")
        
        value = self.values[self.elements_number - 1]
        self.elements_number -= 1
        return value
    
    def first(self):
        if self.__empty_list():
            return print("A fila está vazia!!!")
        
        return self.values[self.elements_number - 1]