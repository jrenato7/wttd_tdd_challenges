# coding: utf-8
"""
1. Se receber um número divisível por 3 fala fizz
2. Se receber um número divisível por 5 fala buzz
3. Se receber um número divisível por 3 e 5 fala fizzbuzz
4. Se não for nenhum dos acima fala o próprio número
"""
from functools import partial

def multiplo_de(base, valor):
    return valor % base == 0


multiplo_de_5 = partial(multiplo_de, 5)
multiplo_de_3 = partial(multiplo_de, 3)


def fizzbuzz(num):
    ret = str(num)
    if multiplo_de_3(num) and multiplo_de_5(num):
        ret = 'fizzbuzz'
    elif multiplo_de_5(num):
        ret = 'buzz'
    elif multiplo_de_3(num):
        ret = 'fizz'
    return ret

assert '1' == fizzbuzz(1)
assert '2' == fizzbuzz(2)
assert '4' == fizzbuzz(4)

assert 'fizz' == fizzbuzz(3)
assert 'fizz' == fizzbuzz(6)
assert 'fizz' == fizzbuzz(9)

assert 'buzz' == fizzbuzz(5)
assert 'buzz' == fizzbuzz(10)
assert 'buzz' == fizzbuzz(20)

assert 'fizzbuzz' == fizzbuzz(15)
assert 'fizzbuzz' == fizzbuzz(30)
assert 'fizzbuzz' == fizzbuzz(45)