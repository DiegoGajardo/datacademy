# Rangos
# el usuario ingresa 3 numeros:
# limite inferior = lim_inf
# limite superior =  lim_sup
# numero de comparacion = comp
# si el numero está entre los lim se imprime en pantalla
# sino se imprime en pantalla y se pide otro numero

def main():
    print("""
    Ingresa 3 numeros que tu quieras y comparemos!
    """)

def rangos(lim_inf, lim_sup, comp):
    while True:
        if (comp >= lim_inf and comp <= lim_sup) or (comp <= lim_inf and comp >= lim_sup):
            print("\nGEnial! El numero", comp, " está en este rango!")
            break
        else:
            print("\nEl numero que escogiste es: ", comp)
            comp = int(input("\nIngresa otro numero para comparar: "))

def run():
    main()
    lim_inf = int(input("Ingresa un numero: "))
    lim_sup = int(input("Ingresa otro numero: "))
    comp = int(input("\nIngresa un numero para comparar: "))
    rangos(lim_inf, lim_sup, comp)

if __name__ == '__main__':
    run()