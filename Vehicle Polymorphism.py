class BMW:
    def fuel_type(self):
        print("BMW uses Petrol or Diesel.")

    def max_speed(self):
        print("BMW maximum speed is 250 km/h.")

class Ferrari:

        def fuel_type(self):
            print("Ferrari uses high-performance Petrol.")

        def max_speed(self):
            print("Ferrari maximum speed is 340 km/h.")

car1 = BMW()
car2 = Ferrari()

for car in (car1, car2):
     car.fuel_type()
     car.max_speed()