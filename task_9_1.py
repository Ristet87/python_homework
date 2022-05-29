import time

class TrafficLight:
    _color = 'red', 'yellow', 'green'

    def running(self):
        while True:
            print('red')
            time.sleep(7)
            print('yellow')
            time.sleep(2)
            print('green')
            time.sleep(5)

a = TrafficLight()
print(a.running())