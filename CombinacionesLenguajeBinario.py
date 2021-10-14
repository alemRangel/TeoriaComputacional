import matplotlib.pyplot as plt
import numpy as np
import random

def combinaciones_lenguaje_binario(n):
    length_of_for = pow(2, n)
    print("Tamaño potencia")
    print(length_of_for)
    fo = open("logs/universoBinario/universeBinaryLanguage.txt", "w")
    fo.write("{[]")
    for x in range(1, int(length_of_for)):
        bin_str = bin(x).split("b")[1]
        print(bin_str)
        bin_str_zero = zero_at_start(bin_str)
        if x == 1:
            str_to_file = "," +  bin_str + "," + bin_str_zero
        else:
            str_to_file = bin_str + "," + bin_str_zero
        if x + 1 != length_of_for:
            str_to_file = str_to_file + ","

        fo.write(str_to_file)

    fo.write("}")
    fo.close()


def zero_at_start(bin_str):
    list_number = list(bin_str)
    list_number[0] = "0"
    print("".join(list_number))
    return "".join(list_number)


def graph():
    fo = open("logs/universoBinario/universeBinaryLanguage.txt", "r")
    cont = True
    string_aux = ""
    set_of_ones = []
    print("Creando gráfica")
    while(cont):
        char = fo.read(1)
        if not char:
            print("Terminé de leer")
            cont = False
            fo.close()
        else:
            if char == "," or char == "}":
                set_of_ones.append(string_aux.count("1"))
                string_aux = ""
            else:
                string_aux = string_aux + char

    print("Ando graficando papi")

    plt.scatter(np.array(range(len(set_of_ones))), set_of_ones)
    set_of_ones.clear()
    plt.show()

if __name__ == "__main__":
    print("Programa que genera el universo del lenguaje binario con cadenas de longitud n (0<=n<=1000)")
    continua = True
    while (continua):
        opc = True
        while opc:
            print("Introduzca una opción para ejecutar el programa")
            print("1- Ejecutar el programa con un input suyo")
            print("2- Ejecutar el programa con un input aleatorio")
            opc_sel = input()
            if opc_sel == "1":
                print("Introduzca una n")
                n = input()
                combinaciones_lenguaje_binario(int(n))
                print("Se ejecutó el universo del lenguaje binario hasta con cadenas de longitud:" + str(n))
                opc = False
            elif opc_sel == "2":
                rand_int = random.randint(1, 1000)
                combinaciones_lenguaje_binario(rand_int)
                opc = False
                print("Se ejecutó el universo del lenguaje binario hasta con cadenas de longitud:" + str(rand_int))

        graph()
        print("¿Desea Ejecutar de nuevo el programa? Y/N")
        continua_char = input()
        if continua_char == "Y":
            continua = True
        else:
            continua = False

    print("Has generado un pedazo de universo del lenguaje binario")
