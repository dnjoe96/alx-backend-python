#!/usr/bin/env python3
""" Module contains function to returns a function """
from typing import Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Functions return a function """
    def innerFunc(number):
        return multiplier * number
    return innerFunc
