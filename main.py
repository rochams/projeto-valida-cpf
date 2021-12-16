# VALIDADOR DE CPF:
import re
from validacpf import check_cpf, get_mult, input_clear, lista

while True:

    cpf = input('Digite o CPF: ')
    cpf = input_clear(cpf)
    if cpf.isnumeric() and len(cpf) == 11:
        nove_digitos = cpf[:-2]
    else:
        msg = 'Por favor, digite apenas números' if not cpf.isnumeric() else 'Erro! Digite novamente.'
        print(msg)
        continue
    
    # print(nove_digitos)                     Check de funcionamento da variável e filtros.

    soma_digito_1 = get_mult(nove_digitos, lista)

    digito_1 = '0' if 11 - soma_digito_1 % 11 > 9 else str(11 - soma_digito_1 % 11)

    dez_digitos = nove_digitos + digito_1

    soma_digito_2 = get_mult(dez_digitos, lista)

    digito_2  = '0' if 11 - soma_digito_2 % 11 > 9 else str(11 - soma_digito_2 % 11)

    cpf_checado = dez_digitos + digito_2

    print(check_cpf(cpf, cpf_checado))

