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


def clean_str(text, chars_to_check, chars_to_delete=" \t\r", error_msg="Unknown char found: "):
    res = []

    for char in text:
        if char in chars_to_check:
            res.append(char)
        elif char in chars_to_delete:
            pass
        else:
            raise ValueError(error_msg + char)

    return ''.join(res)
