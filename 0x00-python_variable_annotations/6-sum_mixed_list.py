#!/usr/bin/env python3
""" Module contains function to return sum of items in a list """
from typing import Union, List

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Functions return sum of items in a list """
    return sum(mxd_lst)
