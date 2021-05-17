import math

def tipo_triangulo(beta,alpha):
    base_mitad = str(input("""
    La altura está en la mitad de la base?
    si o no
    
    """)).lower().strip()

    if (base_mitad == "si"):
        
        if (beta  == 60 and alpha == 60):
            print("Es un triangulo rectangulo")
        elif(beta == alpha):
            print("Es un triangulo isosceles")
    else:
        print("Es un triangulo escaleno")

def triangulo(base,altura):
    area = (base * altura) / 2

    beta = round(math.atan(altura/(base/2) ), 2)
    alpha = round(math.atan(altura/(base/2) ), 2)

    tipo_triangulo(beta, alpha)

    print("El area es: ", area, "\n")


def run():
    b = float(input("Ingresa la base del triangulo: "))
    h = float(input("Ingresa la altura del triangulo: "))
    triangulo(b,h)

if __name__ == '__main__':
    run()