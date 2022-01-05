import random, time, sys
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

number_of_str = 100

def generar_cadenas():
    print("Generando cadenas......")
    size_of_str = 64
    f_total = open("logs/protocolo/protocoloTotal.txt", "a")
    for i in range(number_of_str):
        aux_str = ""
        if i % 50000 == 0:
            print("Ando chambeando papi...")

        for j in range(size_of_str):
            rand_int = random.randint(0, 1)
            aux_str = aux_str + str(rand_int)
        aux_str = aux_str + "\n"
        f_total.write(aux_str)
    f_total.close()
    print("Cadenas Generadas")


def classify_strings(veces_ejecutadas):
    f_total = open("logs/protocolo/protocoloTotal.txt", "r")
    f_correct = open("logs/protocolo/protocoloCorrectas.txt", "a")
    f_incorrect = open("logs/protocolo/protocoloIncorrectas.txt", "a")

    lines = f_total.readlines()
    i = 0
    for line in lines:
        length_line = len(line)
        state = 0
        i = i + 1
        if i % 50000 == 0:
            print("Sigo chambeando papi....")

        if i > int(number_of_str * veces_ejecutadas):

            for x in range(length_line):
                character = line[x]
                if state == 0:
                    if character == "0":
                        state = 2
                    elif character == "1":
                        state = 1
                elif state == 1:
                    if character == "0":
                        state = 3
                    elif character == "1":
                        state = 0
                elif state == 2:
                    if character == "0":
                        state = 0
                    elif character == "1":
                        state = 3
                elif state == 3:
                    if character == "0":
                        state = 1
                    elif character == "1":
                        state = 2

                if x + 1 == length_line:
                    if state == 0:
                        f_correct.write(line)
                    else:
                        f_incorrect.write(line)

    f_total.close()
    f_correct.close()
    f_incorrect.close()


def pintar_grafo():
    print("Creando Grafo")
    df = pd.DataFrame({'from': ['Inicio', 'Activo', 'txt', 'q0', 'q1', 'q0', 'q2', 'q1', 'q3', 'q2', 'q3', 'q0'],
                       'to': ['Activo', 'txt', 'q0', 'q1', 'q0', 'q2', 'q0', 'q3', 'q1', 'q3', 'q2', 'Activo']})

    graph = nx.from_pandas_edgelist(df, 'from', 'to', create_using=nx.DiGraph())
    nx.draw(graph, with_labels=True, node_size=1500, node_color="skyblue", pos=nx.fruchterman_reingold_layout(graph),
            arrows=True)
    plt.title("Automata_Protocolo_AFDParidad")
    plt.show()


if __name__ == "__main__":
    veces_ejecutadas = 0
    cont = "Y"
    print("Bienvenido al programa protocolo")
    while cont == "Y":
        generar_cadenas()
        print("Esperando para continuar con el AFD de paridad")
        time.sleep(1)
        classify_strings(veces_ejecutadas)
        print("Las cadenas ya pasaron por el autómata")
        print("Desea graficar el autómata? (Y/N)")
        graph = input()
        if graph == "Y":
            pintar_grafo()
        print("Desea crear más cadenas y pasarlas por el autómata? (Y/N)")
        cont = input()
        veces_ejecutadas = veces_ejecutadas + 1


    print("Terminamos, gracias por usarme c:")
