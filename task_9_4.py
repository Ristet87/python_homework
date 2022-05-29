class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Car is on the ride')

    def stop(self):
        print('Car has stopped')

    def turn(self):
        print('Car turned')

    def show_speed(self):
        return print(f'Current speed is {self.speed}.')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print('You drive too fast')
        else:
            print(f'Current speed is {self.speed}.')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print('You drive too fast')
        else:
            print(f'Current speed is {self.speed}.')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


a = Car(70, 'white', 'Emobile', False)
a.show_speed()
a.go()
b = TownCar(75, 'green', 'Fiat', False)
b.show_speed()
b.stop()
print(b.is_police)
c = PoliceCar(90, 'black', 'Ford', True)
c.show_speed()
print(c.is_police)
