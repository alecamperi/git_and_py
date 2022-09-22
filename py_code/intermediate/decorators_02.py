# Ejemplo N:1
# def decorator(func):
#     def wrapper():
#         print("Esto se añade a mi funcion original")
#         func()
#     return wrapper

# @decorator
# def hello():
#     print("Hello..")

# # hello = decorator(hello)
# hello()

# --------------------------------------------
# --------------------------------------------
# Ejemplo N:2
# def mayusculas(func):
#     def envoltura(texto):
#         return func(texto).upper()
#     return envoltura

# @mayusculas
# def mensaje(nombre):
#     return f'{nombre}, recibiste un mensaje'

# print(mensaje("Cesar"))
# --------------------------------------------
# --------------------------------------------
# # Ejemplo N:3
