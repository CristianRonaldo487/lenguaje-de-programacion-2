import math

def main():

        if a <= 0 or b <= 0:
            raise ValueError("Los catetos deben ser positivos.")
        
        h = math.sqrt(a**2 + b**2)

        area = (a * b) / 2
        perimetro = a + b + h

        print(f"cateto A: {a}")
        print(f"cateto B: {b}")
        print(f"hipotenusa: {h:.2f}")
        print(f"area: {area:.2f}")
        print(f"perimetro: {perimetro:.2f}")


        except ValueError as ve:
            print("error:", ve)

if __name__=="__main__":
    main()


        
        
        

        
        
        
        


