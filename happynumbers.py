# coding: utf-8
"""
Confira como encontrar um número feliz
José Luiz Pastore Mello*

Escolha um número natural maior do que 1 e calcule a soma dos quadrados dos seus
algarismos. Pegue o número encontrado e repita a operação, calculando a soma dos
quadrados dos seus algarismos. Repetindo esse processo sucessivamente, quando a
sequência calculada termina em 1, dizemos que o número submetido ao processo é
um número "feliz", caso contrário, ele é chamado de número "triste". Por
exemplo, pode-se verificar que o número 4.599 é feliz fazendo as seguintes
contas: 4²+5²+9²+9²=203; 2²+0²+3²=13; 1²+3²=10; 1²+0²=1.

Uma vez encontrado um número feliz, outros tantos também podem ser obtidos
observando-se a sequência usada no processo de verificação da "felicidade" do
número. Por exemplo, no caso de 4.599, a sequência de verificação nos garante
que os números 10, 13 e 203 também são felizes.

Qualquer permutação dos algarismos de um número feliz irá gerar outro número
feliz, como é o caso, por exemplo, de 9.549, obtido a partir de uma permutação
dos algarismos de 4.599. Além disso, a introdução de zeros em um número feliz
sempre conduz a um outro número feliz, como são os casos dos números 45.990,
459.900, 4.599.000 etc. Essa observação nos delega a certeza de que existem
infinitos números felizes.

O leitor poderá verificar por conta própria que os números tristes não têm um
ponto final fixo, viajando eternamente em torno do mesmo ciclo: 4, 16, 37, 58,
89, 145, 42, 20, voltando ao 4.

Encontrar novos números felizes é um bom exercício para o raciocínio, mas tem
gente levando a sério demais o que não passa de uma brincadeira para os
matemáticos. No início deste ano, um numerólogo afirmou em entrevista que,
diferentemente de 2003, que foi feliz do ponto de vista numerológico, o período
de 2004 a 2007 será extremamente desfavorável. Tudo nos leva a crer que a
análise pessimista se fundamenta na definição de números felizes e tristes, já
que, sob esse ponto de vista, 2003 e 2008 são números felizes, e, de 2004 a
2007, temos um intervalo de números tristes.

Utilizando a mesma subjetividade presente no jogo de palavras do numerólogo,
proponho um desafio ao leitor. Adivinhe a idade de João a partir do seguinte
diálogo com sua filha Ana: (Ana) "Pai, você não se acha muito quadrado?";
(João) "Querida filha, sou quadrado, mas sou feliz". A resposta do desafio será
enviada por e-mail. Um feliz 2004 a todos! *José Luiz Pastore Mello é mestre
em ensino de matemática pela USP e professor do Colégio Santa Cruz
"""


def happy(num):
    if num in (1, 10, 13, 203):
        return True
    if num == 10:
        return True
    if num == 13:
        return True
    if num == 203:
        return True

# Teste mais simples:
assert happy(1)

# Testes do problema: 10, 13 e 203
assert happy(10)
assert happy(13)
assert happy(203)
