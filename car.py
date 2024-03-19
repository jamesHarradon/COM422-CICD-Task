from vehicle import Vehicle

class Car(Vehicle):

    def calculate_fee(self):
        if self.weight > 1590:
            extra = round(self.weight - 1590 / 100)/10
            return 5 + extra
        return 5