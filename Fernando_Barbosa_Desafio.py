
numero_atual = ''
numero_maior = 0
resp = 'Ss'


def anterior(digit):
    if digit == 0:
        return 9

    return digit-1


print('=-='*20)
while resp in 'Ss':
    entrada = int(input('Digite um número qualquer --> '))
    for digit in str(entrada):
        if len(numero_atual) > 0 and int(numero_atual[-1]) == anterior(int(digit)):
            numero_atual += digit
        else:
            numero_atual = digit

        if int(numero_atual) > numero_maior:
            numero_maior = int(numero_atual)

    print(
        f'O maior número formado por dígitos consecutivos de {entrada} é \033[31m{numero_maior}\033[0;0m ')
    print('=-='*20)
    resp = str(input('Você quer continuar? [S/N] '))
