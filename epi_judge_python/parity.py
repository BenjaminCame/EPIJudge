from tkinter import Y
from test_framework import generic_test


def parity(x: int) -> int:
    y: int
    y = x ^ (x >> 1)
    y = y ^ (y >> 2)
    y = y ^ (y >> 4)
    y = y ^ (y >> 8)
    y = y ^ (y >> 16)
    return y&1


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
