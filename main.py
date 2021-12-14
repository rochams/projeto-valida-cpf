# VALIDADOR DE CPF:
import re

from validacpf import input_clear

while True:

    cpf = input('Digite o CPF: ')
    cpf = input_clear(cpf)
    if cpf.isnumeric() and len(cpf) == 11:
        nove_digitos = cpf[:-2]
    else:
        if not cpf.isnumeric():
            print('Por favor, digite apenas números.')
        else:
            print('Erro! Digite novamente.')
        continue
    
    print(nove_digitos)                     # Check de funcionamento da variável e filtros.

    lista_nove_dig = []
    for d in nove_digitos:                  # Função para lançar os valores na lista
        lista_nove_dig.append(d)            # Insere cada item dentro da lista
    # print(lista_nove_dig)                 # Checagem se a lista está correta.
    soma = 0
    n = 10                                  # Variável criada para ser usada no for in a seguir, pois irá ser multiplicada por cada um dos dígitos do cpf inserido.
    for d in lista_nove_dig:                # For...in para guardar a soma das multiplicações dos dígitos dos 9 primeiros dígitos com os contadores criados.
        m = int(d) * int(n)                 
        soma = int(soma) + m
        n -= 1
    if (11 - (int(soma) % 11)) > 9:         # Verificador do primeiro dígito (com a fórmula)
        digito1 = 00
    else:
        digito1 = 11 - (int(soma) % 11)     # Cálculo para verificar qual o 10º caractere.
    lista_nove_dig.append(str(digito1))
    n = 11
    soma = 0
    for d in lista_nove_dig:                # For...in para guardar a soma das multiplicações dos dígitos dos 10 primeiros dígitos com os contadores criados.
        m = int(d) * int(n)
        soma += m
        n-= 1
    if 11 - (soma % 11) > 9:                # Condição para saber 
        digito2 = 0
    else:
        digito2 = 11 - int((soma % 11))
    lista_nove_dig.append(str(digito2))     # Inserindo o dígito, que foi verificado, na lista.
    print(lista_nove_dig)
    novo_cpf = ''.join(lista_nove_dig)      # Transformando a lista com os dígitos do cpf em uma string.
    print(novo_cpf)
    msg = 'CPF válido!' if int(novo_cpf) == int(cpf) else 'CPF inválido!'    # Mensagem a ser exibida
    print(msg)
