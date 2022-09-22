# def make_repeater_of(n):
#     def repeater(string):
#         assert type(string) == str, 'Solo puedes repetir cadenas'
#         return string * n
#     return repeater


# def run():
#     repeat_5 = make_repeater_of(5)
#     print(repeat_5('Hola'))


# if __name__ == '__main__':
#     run()

def make_division_by(n:int)-> int:
    return lambda x: round(x/n)

def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))

if __name__ == '__main__':
    run()