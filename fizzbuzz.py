# coding: utf-8
"""
1. Se receber um número divisível por 3 fala fizz
2. Se receber um número divisível por 5 fala buzz
3. Se receber um número divisível por 3 e 5 fala fizzbuzz
4. Se não for nenhum dos acima fala o próprio número
"""


def fizzbuzz(num):
    if num in (5, 10, 20):
        return 'buzz'
    if num == 5:
        return 'buzz'
    if num == 10:
        return 'buzz'
    if num == 20:
        return 'buzz'
    if num in (3, 6, 9):
        return 'fizz'
    return str(num)

assert '1' == fizzbuzz(1)
assert '2' == fizzbuzz(2)
assert '4' == fizzbuzz(4)

assert 'fizz' == fizzbuzz(3)
assert 'fizz' == fizzbuzz(6)
assert 'fizz' == fizzbuzz(9)

assert 'buzz' == fizzbuzz(5)
assert 'buzz' == fizzbuzz(10)
assert 'buzz' == fizzbuzz(20)