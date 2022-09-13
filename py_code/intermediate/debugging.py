def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    try:
        num = int(input('Ingresa un número: '))
        assert num > 0, "Ingresa un numero positivo"
        if num < 0:
            # raise Exception("Ingresa un numero positivo")
            pass
        else:
            print(divisors(num))
            print("Terminó mi programa")
    except ValueError:
        print("Solo puedes añadir numeros")
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    run()