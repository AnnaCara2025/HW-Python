import math

def square(side):
    area = side * side
    if isinstance(side, int):
        return int(area)
    else:
       return math.ceil(area)
side_input = float(input("Введите длину стороны квадрата: "))
result = square(side_input)
print(f"Площадь квадрата: {result}")
