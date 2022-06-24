#!/usr/bin/env python3
""" Module containing function that returns list's first element or None"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """A function that returns each element replicated
    to factor list from lst"""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
