import math

def f(x):
    r = (x ** 3) - math.sin(x)
    return r

def ddf(x):
    r = 0 - math.sin(x) ## devirada quarta
    return r

def SimpsonSimples():
    a = 0  # Limite Inferior
    b = 1  # Limite Superior
    n = 4
    h = (b - a) / (2 * n)  # H = (limiteSuperior - limiteInferior) / 2
    x1 = (b + a) / 2 # definindo valor para iteracao no calculo de integral
    # ***********************************************************************************
    listaY = []
    listaYMod = []
    i = a  # i igual a limiteInferior
    maxi = 0
    while i <= b:  #enquanto i for menor ou igual a b
        listaY.append(f(i))
        listaYMod.append(abs(ddf(i)))
        i = i + h

    # Calculando integral por n = 4

    it1 = (h / 3) * (listaY[0] + 4 * listaY[1] + listaY[2])
    it2 = (h / 3) * (listaY[2] + 4 * listaY[3] + listaY[4])
    it3 = (h / 3) * (listaY[4] + 4 * listaY[5] + listaY[6])
    it4 = (h / 3) * (listaY[6] + 4 * listaY[7] + listaY[8])

    it = it1 + it2 + it3 + it4  # resultado aplicado a it

    maxi = max(listaYMod)
    erro = n * ((h ** 5)/90) * maxi

    print('f(x) = x^3 - sen(x)')
    print('Limite a: {}\tLimite b: {}\tN: {}'.format(a, b, n))
    print('Resultado da Integral aproximada: {}'.format(it))
    print('Erro: {}\n'.format(erro))


#INICIO DO PROGRAMA
print('\n------------- MÉTODO DO SIMPSON REPETIDO ------------\n')
SimpsonSimples()
