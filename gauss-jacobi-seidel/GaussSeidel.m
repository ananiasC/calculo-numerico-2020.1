% ALGORITMO DE  GAUSS SEIDEL

disp('Algoritmo de Gauss Seidel')

A = [5 -1 0 0;-1 4 -1 0;0 -1 4 -1;0 0 -1 5;]; % Matriz A
b = [1 -2 3 4]; % vetor b
m = 50; %VALOR MÁXIMO DE ITERAÇÕES
e = 0.001; % ERRO DESEJADO
x = input('Digite o valor de início para o método:')

N = 20; %INICIANDO COM UM VALOR MAIOR QUE ERRO
ni = 0; %NUMERO DE ITERAÇÕES

% VALIDANDO CONVERGÊNCIA PELO CRITÉRIO DE LINHAS DO MÉTODO DE SEIDEL
alf1 = (abs(A(1,2)) + abs(A(1,3)) + abs(A(1,4))) / abs(A(1,1));
alf2 = (abs(A(2,1))*alf1 + abs(A(2,3)) + abs(A(2,4))) / abs(A(2,2));
alf3 = (abs(A(3,1))*alf1 + abs(A(3,2))*alf2 + abs(A(3,4))) / abs(A(3,3));
alf4 = (abs(A(4,1))*alf1 + abs(A(4,2))*alf2 + abs(A(4,3))*alf3) / abs(A(4,4));

alf = [alf1 alf2 alf3 alf4];
convergencia = (max(alf));

%INFORMANDO SE O SISTEMA CONVERGE
if (convergencia > 1)
    disp('Não existe garantias de convergência pelo método de Gauss Seidel.');
    disp(convergencia);
else
    disp('Existe garantias de convergência pelo método de Gauss Seidel.');
    disp(convergencia);
end;

while (N > e) && ni < (m-1)
    %CALCULANDO O Y PARA SE OBTER O ERRO PARA COMPARAÇÃO DE PONTO DE PARADA
    y1 = (b(1) - A(1,2) * x(2) - A(1,3) * x(3) - A(1,4) * x(4)) / (A(1,1));
    y2 = (b(2) - A(2,1) * y1 - A(2,3) * x(3) - A(2,4) * x(4)) / (A(2,2));
    y3 = (b(3) - A(3,1) * y1 - A(3,2) * y2 - A(3,4) * x(4)) / (A(3,3));
    y4 = (b(4) - A(4,1) * y1 - A(4,2) * y2 - A(4,3) * y3) / (A(4,4));
    
    y = [y1 y2 y3 y4];
    
    %ERRO SENDO CALCULADO BASEADO NA NORMA EUCLIDIANA
    N = sqrt((x(1) - y(1))^2 + (x(2) - y(2))^2 + (x(3) - y(3))^2 +(x(4) - y(4))^2);
    ni = ni + 1;
    
    %IMPRIMINDO NO TERMINAL DE COMANDO OS RESULTADOS OBTIDOS
    disp('iteração:');
    disp(ni);
    disp('x:');
    disp(x);
    disp('y:');
    disp(y);
    disp('erro atual:');
    disp(N);
    
    x = y;
    
    %ACRESCENTANDO ERRO ATUAL EM UM VETOR DE ERROS
    err(ni) = N;
    
end
%PLOTANDO OS ERROS OBTIDOS EM GRÁFICO
hold on
plot(err)
plot(err,'*b')
title('Erro com o passar de iterações:')
xlabel('Iterações')
ylabel('Erro dado em N')
grid