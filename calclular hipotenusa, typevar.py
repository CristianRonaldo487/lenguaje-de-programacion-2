from typing import TypeVar
import math

T = TypeVar('T', int, float)

def calcular_hipotenusa(cateto_a: T,cateto_b: T) -> T:
    return math.sqrt(cateto_a**2 + cateto_b**2)
def main():
    try:
        a = int(imput("ingrese el valor del cateto A: "))
        b = int(imput("ingrese el valor de cateto b: "))

print("hipotenusa =",calcular_hipotenusa(3,4))
print("hipotenusa =",calcular_hipotenusa(5.5,2.2))




