class car:
    def __init__(self, speed, color, name):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = False


    def go(self):
        print(f"{self.name} is go ")

    def stop(self):
        print(f"{self.name} is stop ")

    def turn(self,directory):
        print(f"{self.name} is turn to {directory} ")

class TownCar(car):
    pass

class WorkCar(car):
    pass

class SportCar(car):
    pass

class PoliceCar(car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.name = "Police car"
        self.is_police = True
        print("Это полиция, пора бежать")


car1 = PoliceCar(100, "blue","ewqrt")
car2 = SportCar(190,"yellow","moya")
car3 = TownCar(123,"grey","Для жены")


