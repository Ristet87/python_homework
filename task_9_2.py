class Road:
    weight_asphalt_per_unit = 25
    asphalt_layer = 5

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def weight_asphalt(self):
        return f'{self.__length} м * {self.__width} м * {Road.weight_asphalt_per_unit} кг * {Road.asphalt_layer} см = ' \
               f'{int(self.__length * self.__width * Road.weight_asphalt_per_unit * Road.asphalt_layer/1000)} т.'

a = Road(20, 5000)
print(a.weight_asphalt())
