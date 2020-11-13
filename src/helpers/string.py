'''
Some helpers for main scripts.
'''

from typing import List

def subscript_it(string: str) -> str:
    '''
    Turns `5` into `₅`
    '''

    subs = '₀₁₂₃₄₅₆₇₈₉'

    res: List[str] = []

    for char in string:
        if char.isdigit():
            res.append(subs[int(char)])
        else:
            res.append(char)
    
    return ''.join(res)


def clean_str(string: str, chars_to_del: str):
    res = []

    for char in string:
        if not char in chars_to_del:
            res.append(char)

    return ''.join(res)

def clean_ws(string: str) -> str:
    return clean_str(string, ' \n\r')
