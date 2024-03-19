from abc import ABC, abstractmethod

class Vehicle:
    def __init__(self, reg, weight):
        self.reg = reg
        self.weight = weight

    @abstractmethod
    def calculate_fee(self):
        pass
