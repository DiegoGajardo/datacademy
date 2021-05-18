#Cachipun == Piedra, papel o tijera
#Papel le gana a la Piedra
#Piedra le gana a la Tijera
#Tijera le gana al Papel

def main():
    print("""
    Bienvenido a jugar Piedra, Papel o Tijera! 

Elige entre estas opciones: 
        piedra
        papel
        tijera

Quien gane 2 de 3 partidas será el ganador. Suerte!!

        """
    )

def cachipun(player1, player2):
    games_player1 = 0
    games_player2 = 0
    while (games_player1 != 2) or (games_player2 != 2):
        if player1 == "papel" and player2 == "piedra":
            games_player1 += 1
            print("\nJugador 1 ganó la partida!\n")
        elif player1 == "papel" and player2 == "tijera":
            games_player2 += 1
            print("\nJugador 2 ganó la partida!\n")
        elif player1 == "papel" and player2 == "papel":
            print("\nEmpate!\n")
        elif player1 == "piedra" and player2 == "piedra":
            print("\nEmpate!\n")
        elif player1 == "piedra" and player2 == "tijera":
            games_player1 += 1
            print("\nJugador 1 ganó la partida!\n")
        elif player1 == "piedra" and player2 == "papel":
            games_player2 += 1
            print("\nJugador 2 ganó la partida!\n")
        elif player1 == "tijera" and player2 == "piedra":
            games_player2 += 1
            print("\nJugador 2 ganó la partida!\n")
        elif player1 == "tijera" and player2 == "tijera":
            print("\nEmpate!\n")
        elif player1 == "tijera" and player2 == "papel":
            games_player1 += 1
            print("\nJugador 1 ganó la partida!\n")
        
        if games_player1 == 2:
            print("El jugador 1 es el GANADOR!")
            break
        elif games_player2 == 2:
            print("El jugador 2 es el GANADOR!")
            break

        player1 = str(input("Jugador 1 escoge una opción: "))
        player2 = str(input("Jugador 2 escoge una opción: "))
    

def run():
    main()
    player1 = str(input("Jugador 1 escoge una opción: "))
    player2 = str(input("Jugador 2 escoge una opción: "))
    cachipun(player1,player2)


if __name__ == '__main__':
    run()