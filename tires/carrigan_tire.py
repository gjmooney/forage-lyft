from tires.tire import Tire

# Service if any value is >= 0.9
class CarriganTire(Tire):
    def __init__(self, wear_array):
        self.wear_array = wear_array

    def needs_service(self):
        if any(value >= 0.9 for value in self.wear_array):
            return True
        else:
            return False
