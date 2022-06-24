#!/usr/bin/env python3
""" Module contains function to returns a function """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ A function to get elements and length as a tuple"""
    return [(i, len(i)) for i in lst]
