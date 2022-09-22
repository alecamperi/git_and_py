# Ejemplo N:1
# FALLBACK_PHONE = '+e00000000'

# def get_phone():
# 	phone = input('Give me your phone: ')
# 	if not phone:
# 		return FALLBACK_PHONE.round()
# 	return int(phone)

# def run():
# 	my_phone = get_phone()
# 	print(f'Your phone is: {my_phone}')

# run()

# --------------------------------------------
# --------------------------------------------
# # Ejemplo N:2 --> Pruba de numeros primos
def is_primo(num:int) -> bool:
    result = [i for i in range(1, num+1) if num%i==0]
    return len(result)==2
    
    # if (num%2 != 0) or (num == 2):
    #     return True
    # else:
    #     return False

def run():
    num = int(input("Ingrese un numero: "))
    print(is_primo(num))

if __name__ == '__main__':
    run()