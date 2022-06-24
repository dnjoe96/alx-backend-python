#!/usr/bin/env python3
""" Module contains function to returns a function """
from typing import List, Union, Tuple, Callable


def element_length(lst: List[List[str]]) -> List[Tuple[str, int]]:
    return [(i, len(i)) for i in lst]
