% Passo 1 - registrando x e y (dados do nosso experimento)

x = [-2 -1 0 1 2 3]';
n = length(x);
y = [19.01 3.99 -1.00 4.01 18.99 45.00]';

% Passo 2 - Plot de Dados
figure(1)

hold on
plot(x,y,'o')
title('Posições [x, y]:')
xlabel('Eixo x')
ylabel('Eixo y')
grid

% Passo 3 - Aplicar Método dos Mínimos Quadrados para encontrar os
% parametros (a, b,c, ...).

A = [ones(size(x)) x]; % Preenche a 1ª coluna com 1, preenche a 2ª coluna com x

%soluçãode Ac=y representa reta ya_j=c_1+c_2 x_j
c = A\y; % Gera uma matriz 2x1 - Posicao 1 - 12.4291, Posicao 2 - 5.1417
ya= c(1)+c(2)*x; %g(x) = 12.4291 + 5.1417 * x

% Plotando em nova figura a reta que melhor se ajusta 

figure(2) % Figura 2 com a melhor reta para os pontos

hold on
subplot(1,2,1)
plot(x,y,'og',x, ya,'r')
title('Melhor Reta para os pontos')
legend('y = 12.4291 + 5.1417x')
xlabel('Eixo x')
ylabel('Eixo y')
grid

% Avaliar Erro Médio Quadratico

e = y - ya
E = sum(e.^2)/n

%---------------------------------------------------------------------
% PARTE DO ALGORITMO PARA DEFINIÇÃO DA PARABOLA PARA OS PONTOS

AP = [ones(size(x)) x x.^2]; % Preenche a 1ª coluna com 1, preenche a 2ª coluna com x, preenche a 3ª coluna com x^2

%soluçãode Ac=y representa reta ya_j=c_1+c_2 x_j
cP = AP\y; % Gera uma matriz 3x1 - Posicao 1 -> -1.1437, Posicao 2 -> 0.0519, Posicao 3 -> 5.0898
yaP= cP(1)+cP(2)*x + cP(3)*x.^2; %k(x) = -1.1437 + 0.0519 * x + 5.0898 * x^2

% Plotando em nova figura a reta que melhor se ajusta 
hold on
subplot(1,2,2)
plot(x,y,'og',x, yaP,'r')
legend('y = -1.1437 + 0.0519x + 5.0898x^2')
title('Melhor Parabola para os pontos')
xlabel('Eixo x')
ylabel('Eixo y')
grid

% Avaliar Erro Médio Quadratico

e_P = y - yaP
E_P = sum(e_P.^2)/n

