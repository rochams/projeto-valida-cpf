import re

class OnlyNumberError(Exception):
    print('Por favor, digite apenas números.')


def input_clear(cpf):
    return re.sub(r'[^0-9]', '', cpf)


def get_sum(cpf, lista):
    s = 0
    for i, n in enumerate(range(10, 1, -1)):
        s += int(cpf[i]) * n
        return s
        
lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]



def get_mult(cpf, lista):
    if len(cpf) == 9:
        mult = zip(cpf, lista[:-1])
        s = 0
        for i in mult:
            s += int(i[0]) * int(i[1])
        return s
    else:
        mult = zip(cpf, lista)
        s = 0
        for i in mult:
            s += int(i[0]) * int(i[1])
        return s



def check_cpf(input_cpf, new_cpf):
    if input_cpf == new_cpf:
        return 'CPF válido!'
    else:
        return 'CPF inválido. Tente novamente.'




if __name__ == '__main__':

    cpf = '031.147.231-10'
    cpf = input_clear(cpf)


    cpf = '031147231'

    soma_digito_1 = get_mult(cpf, lista)

    digito_1 = '0' if 11 - soma_digito_1 % 11 > 9 else str(11 - soma_digito_1 % 11)

    # print(digito_1)

    dez_digitos = str(cpf) + digito_1
    
    # print(dez_digitos)

    soma_digito_2 = get_mult(dez_digitos, lista)

    # print(soma_digito_2)

    digito_2  = '0' if 11 - soma_digito_2 % 11 > 9 else str(11 - soma_digito_2 % 11)

    # print(digito_2)

    cpf_checado = dez_digitos + digito_2

    print(cpf_checado)