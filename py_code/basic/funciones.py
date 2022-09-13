# def imprimir_mensaje():
#     print('Mensaje especial: ')
#     print('¡Estoy aprendiendo a usar funciones!')


# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()


# def conversacion(mensaje):
#     print('Hola')
#     print('Cómo estás')
#     print(mensaje)
#     print('Adios')


# opcion = int(input('Elige una opción (1, 2, 3): '))
# if opcion == 1:
#     conversacion('Elegiste la opción 1')
# elif opcion == 2:
#     conversacion('Elegiste la opción 2')
# elif opcion == 3:
#     conversacion('Elegiste la opción 3')
# else:
#     print('Escribe la opción correcta')

# def suma(a, b):
#     print('Se suman dos números')
#     resultado = a + b
#     return resultado

# sumatoria = suma(1, 4)
# print(sumatoria)

#Ejercicio mejorado de escribir una opcion
import random
opcion = input("Elige una opcion (1, 2, 3): ")

print(""" Hola
    Elegiste la opcion """ + opcion)

def desplegar_opcion(opcion):
    opcion = int(opcion)
    if opcion == 1:
        print("Te doy un numero al azar del 1 al 10: " + str(random.randint(1,10)))
    elif opcion == 2:
        print("Como seleccionaste 2, te recuerdo que Ferrari esta 2do en el campeonato de constructores")
    elif opcion == 3:
        print("El simbolo de mercedes tiene 3 puntas")
    else:
        print("No me jodas, no metiste una opcion del 1 al 3 ....")


desplegar_opcion(opcion)