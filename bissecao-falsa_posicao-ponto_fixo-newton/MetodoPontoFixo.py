import math


# FUNCAO f(x)
def f(x):
    r = math.sin(x) - math.log(x, math.e)  # FUNÇÃO: sen(x) - ln(x)
    return r  # RETORNA O VALOR REAL PARA UM f(x)


# FUNÇÃO g(x)
def g(x):
    r = math.asin(math.log(x, math.e))  # FUNÇÃO: arcsen(ln(x))
    return r


def pontoFixo(xo, erro):
    x = xo
    fx = f(xo)  # função f(x)
    gx = g(xo)  # função de iteração g(x)
    contador: int = 0

    while math.fabs(f(x)) > erro:  # CONDIÇÃO DE PARADA DO WHILE FABS(f(x) < erro
        print('|Execução:{}|x{}:{:.6f}|f(x{}):{:.6f}|g(x{}):{:.6f}|FABS(f(x{})):{:.6f}|'.format(
            contador + 1, contador, x, contador, fx, contador, gx, contador + 1, math.fabs(fx)))
        x = g(x)
        fx = f(x)
        gx = g(x)
        contador = contador + 1
    print('\n')
    return x


# INICIO DO PROGRAMA
print('\n------------- MÉTODO DE PONTO FIXO------------')
print('\nDigite o valor inicial xo')
xo = float(input('xo = '))  # RECEBE O xo - VALOR INICIAL
erro = 0.001
print('erro = {}\n'.format(erro))

raiz = pontoFixo(xo, erro)
print('Raiz aproximada xi: {:.6f}\nf(xi): {:.6f}'.format(raiz, f(raiz)))
