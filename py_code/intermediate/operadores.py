#Prueba de conversion de USD
guaranies = input("Cuántos guaranies tenés?: ")
guaranies = float(guaranies)

valor_dolar = 6847.30
dolares = guaranies / valor_dolar
dolares = round(dolares, 3)
dolares = str(dolares)
print("Tenés: "+dolares+" dolares")



#Prueba de bucles
# n=0
# while n < 10:
#     print(n)
#     n = n + 1