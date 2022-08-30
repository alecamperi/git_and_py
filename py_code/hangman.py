import random
import os

# funcion para limpiar la consola
def clear(): return os.system('cls')

def normalizar(s): 
    reemplazos = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in reemplazos:
        # print(b)
        s = s.replace(a, b).replace(a.upper(), b.upper())
        s = s.lower()
    return s

def read_data():
    palabras = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            # print(line)
            palabras.append(line)
    return palabras

def run():
    # Primero cargar los datos de data.txt en una lista
    palabras = read_data()

    # Luego de cargar, utilizar la libreria random para seleccionar un elemento aleatorio de esa lista, luego normalizamos los caracteres
    num_aleatorio = random.randint(0,170)
    palabra_random = palabras[num_aleatorio].strip()
    palabra_random = normalizar(palabra_random)
    
    # Creamos una lista con guines para añadir las letras que el usuario va acertando
    cantidad_letras = len(palabra_random)
    palabra_a_completar = []
    espacios_por_completar = cantidad_letras
    for i in range(0, cantidad_letras):
        palabra_a_completar.append("_")

    # Luego creamos 2 ciclos para que el usuario vaya haciendo intentos de acierto
    
    finalizado = False
    contador = 0
    while finalizado == False:
        clear()
        print("Adivina la palabra...")
        print(*palabra_a_completar)
        print("-----------------------")
        print("Intentos: " + str(contador)) 
        print("-----------------------")
        seleccion_letra = input("Ingresa una letra: ")
        seleccion_letra = normalizar(seleccion_letra)
        contador = contador + 1

        for i in range(0,cantidad_letras):
            if seleccion_letra == palabra_random[i]:
                palabra_a_completar[i] = seleccion_letra
                espacios_por_completar = espacios_por_completar - 1

        # Condicion para terminar el juego
        if espacios_por_completar == 0:
            clear()
            print(*palabra_a_completar)
            print("")
            print("Completado en el intento número: " + str(contador))
            break
            finalizado = True




if __name__ == '__main__':
    run()