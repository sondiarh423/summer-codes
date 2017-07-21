class Vehicle:
    def __init__(self,Newname):
        self.name = Newname
        self.wheels = 0
        self.ingition = False
        self.passengers = []

    def num_wheels (self, newWheels):
        self.wheels = newWheels

    def ignition (self, key):
        self.ignition = key

    def add_passenger (self, NewPassenger):
        self.passengers.append (NewPassenger)

def main():
    myCar = Vehicle("Mustang")
    myCar.num_wheels(4)
    myCar.add_passenger("Sondia")
    print (myCar.name, myCar.wheels, myCar.passengers)

if __name__=='__main__':
    main()
