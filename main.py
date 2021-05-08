import numpy as np
import sys


def get(a,b):
    c = a
    a = b
    b = c
    return a,b

a,b = get(2,3)
print(f"Before swapping a = 2 & b = 3")
print(f"After swapping  a = {a} & b = {b}")
















