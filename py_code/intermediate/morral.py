def morral(tamano_morral, pesos, valores, n):

    global cont
    cont += 1
    
    print("Se ejecutó una vez... van " + str(cont) + " veces")


    if n == 0 or tamano_morral == 0:
        return 0
    
    if pesos[n - 1] > tamano_morral:
        return morral(tamano_morral, pesos, valores, n - 1)


    valor_1 = valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1)
    valor_2 = morral(tamano_morral, pesos, valores, n - 1)

    print("El valor 1: " + str(valor_1))
    print("El valor 2: " + str(valor_2))
    
    return max(valor_1 , valor_2)


if __name__ == '__main__':
    cont = 0

    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamano_morral = 50
    n = len(valores)
    
    resultado = morral(tamano_morral, pesos, valores, n)
    print(resultado, cont)
    # print(max(1,2))