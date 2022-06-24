#!/usr/bin/env python3
""" Module contains function to returns a tuple """
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Functions return a tuple """
    return (k, float(v))
