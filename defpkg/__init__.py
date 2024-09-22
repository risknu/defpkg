from __future__ import annotations

from typing import Callable, Any
import functools

def eu(func: Callable[..., Any], /) -> Callable[..., Any]:
    "eu?"
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print("\33[1m\33[34meu?\33[0m")
        return func(*args, **kwargs)
    return wrapper

def palitra(func: Callable[..., Any], /) -> Callable[..., Any]:
    """rainbow."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print("".join([
                f"\33[{i}m {i} \33[0m" for i in range(119)
            ])+'\33[0m', sep='', end='\n')
        return func(*args, **kwargs)
    return wrapper

def whatasigma(func: Callable[..., Any], /) -> Callable[..., Any]:
    """Ummm, what's the sigma function?"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print('Umm what the sigma\n💀\n≤))≥\n_| \\_')
        return func(*args, **kwargs)
    return wrapper

def stasikmethod(func: Callable[..., Any], /) -> Callable[..., Any]:
    """Ummmmmm, Stasik method..."""
    @staticmethod
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        return func(*args, **kwargs)
    return wrapper

def commit(func: Callable[..., Any], /) -> Callable[..., Any]:
    """Commit this part of the code, dude."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print('\33[1m\33[35mdid you commit?', '\33[3m\33[90m(edited)', sep='\33[0m', end='\33[0m\n')
        return func(*args, **kwargs)
    return wrapper

def debug_stick(func: Callable[..., Any], /) -> Callable[..., Any]:
    """If it looks like a duck, swims like a duck, and quacks like a duck, it might be... a string in Python."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        function_result: Any = func(*args, **kwargs)
        if function_result is not None:
            print(f'\33[3m\33[90mWell, it seems to me that this is ', 
                    f'\33[1m\33[35m{type(function_result).__name__}',
                sep='\33[0m', end='\33[0m\n')
        return function_result
    return wrapper
