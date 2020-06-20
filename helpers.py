'''
Some helpers for main scripts.
'''

def subscript_it(char):
    '''
    Turns `5` into `₅`
    '''

    digits = '₀₁₂₃₄₅₆₇₈₉'
    if char.isdigit():
        return digits[int(char)]
    else:
        return char
