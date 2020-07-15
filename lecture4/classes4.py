class Flight:
    counter = 1
    def __init__(self,origin,destination,duration):
        self.id=Flight.counter
        Flight.counter+=1

        self.origin=origin
        self.destination=destination
        self.duration=duration

        self.passengers = []

    def print_info(self):
        print(f"Flight Origin : {self.origin}")
        print(f"Flight Destination : {self.destination}")
        print(f"Flight Duration : {self.duration}")
        print()
        print("Passengers Details:")
        for passenger in  self.passengers:
            print(f"{passenger.name}",end=" ")
            print(f"{passenger.flight_id}")

    def Delay(self,amount):
        self.duration+=amount

    def add_passenger(self,p):
        self.passengers.append(p)
        p.flight_id=self.id


class Passenger:
    def __init__(self,name):
        self.name=name

def main():
    # Create flight.
    f1 = Flight(origin="New York", destination="Paris", duration=540)

    # Create passengers.
    alice = Passenger(name="Alice")
    bob = Passenger(name="Bob")

    # Add passengers.
    f1.add_passenger(alice)
    f1.add_passenger(bob)

    f1.print_info()



if __name__=="__main__":
    main()
