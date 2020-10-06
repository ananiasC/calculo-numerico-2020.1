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
    h = (b - a) / 2  # H = (limiteSuperior - limiteInferior) / 2
    x1 = (b + a) / 2 # definindo valor para iteracao no calculo de integral
    # ***********************************************************************************

    it = (h / 3) * (f(a) + 4 * f(x1) + f(b))  # Calculo da integral aproximada

    listaY = []
    i = a  # i igual a limiteInferior
    maxi = 0
    while i <= b:  #enquanto i for menor ou igual a b
        listaY.append(abs(ddf(i)))
        i = i + h
        
    maxi = max(listaY)
    erro = ((h ** 5)/90) * maxi

    print('f(x) = x^3 - sen(x)')
    print('Limite a: {}\tLimite b: {}'.format(a, b))
    print('Resultado da Integral aproximada: {}'.format(it))
    print('Erro: {}\n'.format(erro))


#INICIO DO PROGRAMA
print('\n------------- MÉTODO DO SIMPSON SIMPLES ------------\n')
SimpsonSimples()
