from itertools import count
import time

def fibo_gen(max_num):
    n1 = 0
    n2 = 1
    counter = 0
    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        elif counter == max_num:
            raise StopIteration
        else:
            aux = n1 + n2
            n1, n2 = n2, aux
            counter += 1
            yield aux

if __name__ == '__main__':
    max_num = int(input("Ingrese un numero maximo: "))

    fibonacci = fibo_gen(max_num)
    for element in fibonacci:
        print(element)
        time.sleep(.1)