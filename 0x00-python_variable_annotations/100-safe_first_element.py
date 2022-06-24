#!/usr/bin/env python3
""" Module containing function that returns list's first element or None"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Function returns a list's first element or None"""
    if lst:
        return lst[0]
    else:
        return None
