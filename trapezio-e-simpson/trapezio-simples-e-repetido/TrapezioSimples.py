import math

def f(x):
    r = (x ** 3) - math.sin(x)
    return r

def ddf(x):
    r = 6*x + math.sin(x)
    return r

def TrapezioSimples():
    a = 0  # Limite Inferior
    b = 1  # Limite Superior
    h = b - a  # H = limiteSuperior - limiteInferior
    it = (h / 2) * (f(a) + f(b))  # Calculo da integral aproximada

    listaY = []
    i = a  # i igual a limiteInferior
    maxi = 0
    while i <= b:  #enquanto i for menor ou igual a b
        listaY.append(ddf(i))
        i = i + h

    maxi = max(listaY)
    erro = ((h ** 3)/12) * maxi

    print('f(x) = x^3 - sen(x)')
    print('Limite a: {}\tLimite b: {}'.format(a, b))
    print('Resultado da Integral aproximada: {}'.format(it))
    print('Erro: {}\n'.format(erro))


#INICIO DO PROGRAMA
print('\n------------- MÉTODO DO TRAPÉZIO SIMPLES ------------\n')
TrapezioSimples()
