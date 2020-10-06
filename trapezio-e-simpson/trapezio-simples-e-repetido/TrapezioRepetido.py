import math

def f(x):
    r = x ** 3 - math.sin(x)
    return r

def ddf(x):
    r = 6*x + math.sin(x)
    return r

def TrapezioRepetido():
    a = 0  # Limite Inferior
    b = 1  # Limite Superior
    n = 4  # Número para divisao no trapezio repetido
    h = (b - a) / n  # H = limiteSuperior - limiteInferior

    listaY = []
    listaYMod = []
    i = a  # i igual a limiteInferior
    maxi = 0
    while i <= b:  #enquanto i for menor ou igual a b
        listaY.append(f(i))
        listaYMod.append(abs(ddf(i)))
        i = i + h

    soma = 0
    tamanho = (len(listaY) - 1)
    for i in range(1, tamanho):
        soma = soma + listaY[i]

    it = (h / 2) * (f(0) + listaY[tamanho] + 2 * soma)  # Calculo da integral aproximada

    maxi = max(listaYMod) # valor maximo
    erro = (((b - a) ** 3)/(12 * n**2)) * maxi

    print('f(x) = x^3 - sen(x)')
    print('Limite a: {}\tLimite b: {}\tN: {}'.format(a, b, n))
    print('Resultado da Integral aproximada: {}'.format(it))
    print('Erro: {}\n'.format(erro))


#INICIO DO PROGRAMA
print('\n------------- MÉTODO DO TRAPÉZIO REPETIDO ------------\n')
TrapezioRepetido()
