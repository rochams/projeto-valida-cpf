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
        


if __name__ == '__main__':

    cpf = '031.147.231-10'
    cpf = input_clear(cpf)

