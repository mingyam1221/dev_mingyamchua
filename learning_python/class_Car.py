class Car():
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    # Method drive
    def drive(self, extra_mileage):
        self.mileage = self.mileage + extra_mileage
