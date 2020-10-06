import math


# FUNCAO f(x)
def f(x):
    r = math.sin(x) - math.log(x, math.e)  # FUNÇÃO: sen(x) - ln(x)
    return r  # RETORNA O VALOR REAL PARA UM f(x)


# METODO FALSA POSIÇÃO
def falsaposicao(a, b, erro):
    fa = f(a)  # GRAVA EM VARIAVEL O VALOR PARA f(a)
    fb = f(b)  # GRAVA EM VARIAVEL O VALOR PARA f(b)
    c = (b*fa-fb*a)/(fa-fb)
    fc = f(c)
    contador: int = 0
    print('|Execução:{}|a:{:.6f}|b:{:.6f}|f(a):{:.6f}|f(b):{:.6f}|c:{:.6f}|f(c):{:.6f}|FABS(f(c)):{:.6f}|'.format(contador + 1, a, b, fa,
                                                                                                fb, c, fc, math.fabs(fc)))
    while math.fabs(fc) > erro:  # VALIDAÇÃO DE while ValorAbsolutoDe(f(c)) > erro
        c = (b*fa-fb*a)/(fa-fb)
        fc = f(c)
        if contador > 0:
            print(
                '|Execução:{}|a:{:.6f}|b:{:.6f}|f(a):{:.6f}|f(b):{:.6f}|c:{:.6f}|f(c):{:.6f}|FABS(f(c)):{:.6f}|'.format(
                    contador + 1, a, b, fa, fb, c, fc, math.fabs(fc)))
        if fa * fc < 0:  # CONDIÇÃO DE SUBSTITUIÇÃO DE UM DOS VALORES DO INTERVALO
            b = c
            fb = fc
        else:
            a = c
            fa = fc
        contador = contador + 1
    print('\n')
    return c


print('\n------------- MÉTODO FALSA POSIÇÃO -------------')
print('\nDigite o intervalo [a,b]')
a = float(input('a = '))
b = float(input('b = '))
erro = 0.001
print('erro = {}\n'.format(erro))

# ESTRUTURA CONDICIONAL PARA VALIDAR O INTERVALO
if f(a) * f(b) >= 0:
    print('Intervalo inválido.')
else:  # CASO O INTERVALO SEJA VÁLIDO, ENTAO O PROGRAMA CONTINUA
    c = falsaposicao(a, b, erro)
    print('Raiz aproximada c: {:.6f}\nf(c): {:.6f}'.format(c, f(c)))


