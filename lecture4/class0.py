class Flights:
    
    def __init__(self,origin,destination,duration):
        self.origin=origin
        self.destination=destination
        self.duration=duration

    def Display(self):
        print(self.origin,"to",self.destination,"having duration =",self.duration)


def main():
    f= Flights("New York","Moscow",425)
    f.Display()


if __name__=="__main__":
    main()
