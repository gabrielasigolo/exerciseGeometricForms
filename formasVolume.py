#Author: GabrielaSigolo
from math import pi

print("Choose a geometric shape to know the volume: ")
print("[1] Sphere ")
print("[2] Cub")
print("[3] Parallelepiped")
print("[4] Pyramid ")
answer = int(input("Answer: "))

## answer check
if answer == 1:
    rad = float(input("Type the rad: "))

elif answer == 2:
    side1 = float(input("Type the first side: "))
    side2 = float(input("Type the second side: "))
    side3 = float(input("Type the third side: "))
elif answer == 3:
    lenght = float(input("Type the side A: "))
    width = float(input("Type the side B: "))
    height = float(input("Type the side C: "))
elif answer == 4:
    base = float(input("Type the base: "))
    h = float(input("Type the height: "))
else:
    print("Type a valid number")


## methods
def get_sphere_vol(rad):
    vol = (4 / 3) * pi * rad ** 3
    return vol


def get_cub_vol(side1, side2, side3):
    vol = side1 * side2 * side3
    return vol


def get_parallel_vol(lenght, width, height):
    vol = lenght * width * height
    return vol


def get_pyramid_vol(base, h):
    vol = (1 / 3) * base * h
    return vol


if answer == 1:
    print(get_sphere_vol(rad))
elif answer == 2:
    print(get_cub_vol(side1, side2, side3))
elif answer == 3:
    print(get_parallel_vol(lenght, width, height))
elif answer == 4:
    print(get_pyramid_vol(base, h))
