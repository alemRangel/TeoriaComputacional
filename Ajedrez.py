import random

jugadas_posibles = []
jugadas_ganadoras = []
red_movement = {
    1:"2,5",
    2:"5,7",
    3:"2,4,7",
    4:"7",
    5:"2,10",
    6:"2,5,7,10",
    7:"2,4,10,12",
    8:"4,7,12",
    9:"5,10,13",
    10:"5,7,13,15",
    11:"7,10,12,15",
    12:"7,15",
    13:"10",
    14:"10,13,15",
    15:"10,12",
    16:"12,15"
}

black_movement = {
    1:"6",
    2:"1,3,6",
    3:"6,8",
    4:"3,8",
    5:"1,6,9",
    6:"1,3,9,11",
    7:"3,6,8,11",
    8:"3,11",
    9:"6,14",
    10:"6,9,11,14",
    11:"6,8,14,16",
    12:"8,11,16",
    13:"9,14",
    14:"9,11",
    15:"11,14,16",
    16:"11"
}
def nfa_ajedrez(input, size_actual, estado_actual, jugada_posible):
    posibles_movimientos = []
    if size_actual % 10 == 0:
        print("Ando NFAando jefe")

    if size_actual < len(input):
        if input[size_actual] == "r":
            posibles_movimientos = red_movement[estado_actual].split(",")
        elif input[size_actual] == "b":
            posibles_movimientos = black_movement[estado_actual].split(",")
        for estado in posibles_movimientos:
            jugada_posible_parcial = jugada_posible + "," + str(estado)
            if estado == "16":
                jugadas_posibles.append(jugada_posible_parcial)
                jugadas_ganadoras.append(jugada_posible_parcial)
                return True
            else:
                nfa_ajedrez(input, size_actual + 1, int(estado), jugada_posible_parcial)

    elif size_actual == len(input):
        jugadas_posibles.append(jugada_posible)
        return True


def validar_cadena(cadena_movimientos):
    size_cadena = len(cadena_movimientos)
    array_cadena = cadena_movimientos.split(",")
    print("Validando cadena....")
    if size_cadena == (len(array_cadena)*2 - 1) and len(array_cadena) <= 20:
        for element in array_cadena:
            if element != "r" and element != "b":
                return False
    else:
        return False

    return True


def descomponer_cadena(cadena_movimientos):
    print("Descomponiendo cadena")
    array_movimientos = cadena_movimientos.split(",")
    nfa_ajedrez(array_movimientos, 0, 1, "1")
    fo_total = open("logs/chess/jugadasTotales.txt", "w")
    fo_ganadoras = open("logs/chess/jugadasGanadoras.txt", "w")
    print("Jugadas Totales:")
    for jugada in jugadas_posibles:
        print(jugada)
        fo_total.write(jugada + "\n")

    print("Jugadas Ganadoras:")
    for jugada_ganadora in jugadas_ganadoras:
        print(jugada_ganadora)
        fo_ganadoras.write(jugada_ganadora + "\n")

    fo_ganadoras.close()
    fo_total.close()

    print("Guardando Archivos...")

def generar_cadena_aleatoria():
    size_movimientos_rand = random.randint(1,100)
    cadena_movimientos = ""
    for x in range(size_movimientos_rand):
        rand_character = random.randint(0, 1)
        if rand_character == 0:
            aux_char = "r"
        else:
            aux_char = "b"

        cadena_movimientos = cadena_movimientos + aux_char
        if x < size_movimientos_rand - 1:
            cadena_movimientos = cadena_movimientos + ","
        else:
            print(cadena_movimientos)
            return cadena_movimientos


if __name__ == "__main__":
     print("Juego de ajedrez")
     continua = True
     while continua:
        print("Introduzca una opción para ejecutar el programa")
        print("1- Ejecutar el programa con un input suyo")
        print("2- Ejecutar el programa con un input aleatorio")
        opc_sel = input()
        if opc_sel == "1":
            opc = True
            while opc:
                print("Introduzca una cadena compuesta de movimientos, Red o Black separada por una coma.")
                print("Ejemplo de cadena valida: r,b,r,b,r,r,r,b. Máximo 20 caracteres")
                cadena_movimientos = input()
                if validar_cadena(cadena_movimientos):
                    print("Cadena válida, empezando NDA")
                    descomponer_cadena(cadena_movimientos)
                    opc = False
                else:
                    print("Inserte una cadena válida")

        elif opc_sel == "2":
            print("Empezando a generar cadena aleatoria de movimientos(máximo 100)")
            cadena_movimientos = generar_cadena_aleatoria()
            descomponer_cadena(cadena_movimientos)

        print("¿Desea Ejecutar de nuevo el programa? Y/N")
        continua_char = input()
        if continua_char == "Y":
            continua = True
            jugadas_posibles.clear()
            jugadas_ganadoras.clear()
        else:
            continua = False