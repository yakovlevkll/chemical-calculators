

def a(exp="iyi+ii"):
    if not '+' in exp:
        return("Not a sum")

    b = exp.split('+')
    try:
        nums = [rom2arb(i) for i in b]
    except ValueError as e:
        return(f"Not Roman Numerals - {e}")

    return(sum(nums))


def rom2arb(num):
    valid = "iI"

    for t in num:
        if not t in valid:
            raise ValueError("Unknown Numeral")

    return(len(num))


print(a())
