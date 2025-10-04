class Car:
    def __init__(self):
        self.pos = 0

    def move(self, direction):
        self.pos += direction

    def get_position(self):
        print(self.pos)

class Taxi(Car):
    def __init__(self, cost):
        super().__init__()
        self.cost = cost   
        self.distance = 0  

    def get_total_cost(self):
        print(self.cost * self.distance)

    def reset(self):
        self.distance = 0

    def move(self, direction):
        super().move(direction)
        self.distance += abs(direction)

class Bus(Car):
    def __init__(self, cap):
        super().__init__()
        self.capacity = cap
        self.passengers = []

    def add_passenger(self, destination):
        if len(self.passengers) < self.capacity:
            self.passengers.append(destination)
            return True
        return False
    
    def realease(self):
        self.passengers = [passenger for passenger in self.passengers if passenger != self.pos]

    def get_passenger_count(self):
        return len(self.passengers)

class Trolleybus(Bus):
    def __init__(self, P:int, C:int, L:int, R:int):
        self.pos = int(P)
        self.capacity = int(C)
        self.l = int(L)
        self.r = int(R)
        self.passengers = []
    
    def move(self, direction):
        super().move(direction)

        if self.pos < self.l:
            self.pos = self.l
        if self.pos > self.r:
            self.pos = self.r



def main() -> None:
    inputList:list = input().split()
    n:int = int(inputList[0])
    car = Trolleybus(inputList[1], inputList[2], inputList[3], inputList[4])

    for i in range(n):
        inputList:list = input().split()
        if inputList[0] == "MOVE":
            car.move(int(inputList[1]))

        elif inputList[0] == "POSITION":
            car.get_position()

        elif inputList[0] == "PASSENGER":
            if car.add_passenger(int(inputList[1])) == True:
                print("SUCCESS")
            else: 
                print(":(")

        elif inputList[0] == "PASSENGERS":
            print(car.get_passenger_count())
    
        elif inputList[0] == "RELEASE":
            car.realease()


if __name__ == "__main__":
    main()
