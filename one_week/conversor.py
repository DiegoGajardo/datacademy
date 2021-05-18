#Conversor de millas a kms
# 1 milla = 1.609344 km

def main():
    print("""
    Conversor de distancias

Elige si deseas convertir:
    1. De Kilometros a Millas
    2. De Millas a Kilometros
    3. Salir
    """)

#convierte kilometros a millas
def millas(km):
    mile = (km)/(1.609344)
    print("         ",km, "kilometros en millas es", mile)

#convierte millas a kilometros
def kilometros(mile):
    km = (mile)*(1.609344)
    print("         ",mile,"millas en kilometros es", km)

def run():
    main()
    while True:
        opcion = int(input("\nElige una opción: "))
        if opcion == 1:
            km = float(input("\nIngresa la distancia que quiera convertir a kilometros: "))
            millas(km)
        elif opcion == 2:
            mile = float(input("\nIngresa la distancia que quiera convertir a millas: "))
            kilometros(mile)
        elif opcion == 3:
            print("\nAdios!")
            break
        else:
            print("\nIngresa una opción válida")

if __name__ == '__main__':
    run()