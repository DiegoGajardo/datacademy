#Calculadora de volumenes
#Volumen de un cilindro: V = pi * (radio**2) * h
#Volumen de una esfera: V = (4/3) * pi * (r**3)
#Volumen de un cubo: V = lado**3
#Volumen de una caja: V = largo * ancho * alto

import math

def main():
    print("""
    Bienvenido a la calculadora de volumenes!
    
Estas son las figuras que puedes calcular:
    1. Cilindro
    2. Esfera
    3. Cubo
    4. Caja
    5. Salir
    """)

def cilindro():
    r = float(input("\nIngresa el radio de la figura: "))
    h = float(input("Ingresa la altura de la figura: "))
    volumen = math.pi * (r**2) * h
    print("\nEl volumen calculado es: ", volumen, "\n")

def esfera():
    r = float(input("\nIngresa el radio de la figura: "))
    volumen = (4/3) * math.pi * (r**3)
    print("\nEl volumen calculado es: ", volumen, "\n")
    
def cubo():
    l = float(input("\nIngresa un lado de la figura: "))
    volumen = l**3
    print("\nEl volumen calculado es: ", volumen, "\n")


def caja():
    l = float(input("\nIngresa el largo de la figura: "))
    a = float(input("Ingresa el ancho de la figura: "))
    h = float(input("Ingresa el alto de la figura: "))
    volumen = l * a * h
    print("\nEl volumen calculado es: ", volumen, "\n")


def run():
    main()
    while True:
        opcion = input("Ingresa la opcion de la figura que deseas calcular: ")
        if opcion == "1":
            cilindro()
        elif opcion == "2":
            esfera()
        elif opcion == "3":
            cubo()
        elif opcion == "4":
            caja()
        elif opcion == "5":
            print("\nAdios!")
            break
        else: 
            print("\nIngresa una opcion correcta!\n")


if __name__ == '__main__':
    run()