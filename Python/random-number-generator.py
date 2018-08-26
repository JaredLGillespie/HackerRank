# https://www.hackerrank.com/challenges/random-number-generator/problem

from fractions import Fraction

test_cases = int(input())

for test_case in range(test_cases):
    a, b, c = map(int, input().split())
    p, q = max(a, b), min(a, b)

    if a + b < c:
        ans = Fraction(1, 1)
    elif c <= a and c <= b:
        ans = Fraction(c ** 2, 2 * a * b)
    elif q <= c <= p:
        ans = Fraction((2 * c - q) * q, 2 * a * b)
    else:
        ans = Fraction(1) - Fraction((a + b - c) ** 2, 2 * a * b)

    print('%s/%s' % (ans.numerator, ans.denominator))
