from __future__ import annotations

import functools
from typing import Callable, Any, Optional

def whatasigma(func: Callable[..., Any], /) -> Callable[..., Any]:
    """Ummm, what's the sigma function?"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print('Umm what the sigma\n💀\n≤))≥\n_| \\_')
        return func(*args, **kwargs)
    return wrapper

# TODO: remake `class` from zero, optimizate
def stasikmethod(func: Callable[..., Any], /) -> Callable[..., Any]:
    """Ummmmmm, Stasik method..."""
    @staticmethod
    def wrapper(*args, **kwargs) -> Any:
        return func(*args, **kwargs)
    return wrapper

def commit(func: Callable[..., Any], /) -> Callable[..., Any]:
    """Commit this part of the code, dude."""
    def wrapper(*args, **kwargs) -> Any:
        print('\33[1m\33[35mdid you commit?', '\33[3m\33[90m(edited)', sep='\33[0m', end='\33[0m\n')
        return func(*args, **kwargs)
    return wrapper

@commit
def a(): ...
a()
