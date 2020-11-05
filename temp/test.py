import re

formula = '((C)2(O))3'

brackets_pattern = r'\((.+)\)(\d*)'
brackets_block = re.search(brackets_pattern, formula)


print(brackets_block)
print(brackets_block.groups())
start, stop = brackets_block.span()

print(formula[:start] + formula[stop:])


# sub_1 = Substance('OH')
# sub_2 = Substance('Ba')

# sub_1 * 2
# sub_1 + sub_2

# print(sub_1.composition)
