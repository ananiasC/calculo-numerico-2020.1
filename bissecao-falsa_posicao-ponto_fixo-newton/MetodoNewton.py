import math


# FUNCAO f(x)
def f(x):
    r = math.sin(x) - math.log(x, math.e)  # FUNÇÃO: sen(x) - ln(x)
    return r  # RETORNA O VALOR REAL PARA UM f(x)


# FUNÇÃO f'(x) - devirada de f(x)
def df(x):
    r = math.cos(x) - (1 / x)
    return r


# MÉTODO DE NEWTON
def newton(xo, erro):
    x = xo  # Primeiro x - xo
    fx = f(xo)  # Primeiro f(xo)
    dfx = df(xo)  # Derivada de f(x) - df(xo)
    xi: float
    contador: int = 0

    while math.fabs(f(x)) > erro:  # CONDIÇÃO DE PARADA DO WHILE FABS(f(x) < erro
        xi = x - (fx / dfx)  # Primeiro xi identificado - x1 função de iteração [x - (f(x) / f'(x))]
        fxi = f(xi)
        print('|Execução:{}|x{}:{:.6f}|f(x{}):{:.6f}|x{}:{:.6f}|f(x{}):{:.6f}|FABS(f(x{})):{:.6f}|'.format(
            contador + 1, contador, x, contador, fx, contador + 1, xi, contador + 1, fxi, contador + 1, math.fabs(fxi)))
        contador = contador + 1
        x = xi
        fx = fxi
        dfx = df(x)
    print('\n')
    return x


# INICIO DO PROGRAMA
print('\n------------- MÉTODO DE NEWTON -------------')
print('\nDigite o valor inicial xo')
xo = float(input('xo = '))  # RECEBE O xo - VALOR INICIAL
erro = 0.001
print('erro = {}\n'.format(erro))

raiz = newton(xo, erro)
print('Raiz aproximada xi: {:.6f}\nf(xi): {:.6f}'.format(raiz, f(raiz)))
