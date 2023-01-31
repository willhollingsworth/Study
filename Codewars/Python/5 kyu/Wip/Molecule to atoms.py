import codewars_test as test
# wip
# https://www.codewars.com/kata/52f831fa9d332c6591000511/train/python
# currently works for basic formulas but not brackets

def parse_molecule (formula):
    out_dict = {}
    f_length = len(formula)
    for c,i in zip(formula,range(f_length)):
        start,end  = True,False
        if i !=  0 : start = False
        if i+1 == f_length : end = True
        if not end : next_c = formula[i+1]
        if not start : prev_c = formula[i-1]
        if c.isalpha():
            if c not in out_dict.keys():
                out_dict[c] = 0
            if next_c.isalpha() and not end:
                out_dict[c] += 1
            if end:
                out_dict[c] += 1
        elif c.isdigit():
            if prev_c.isalpha():
                out_dict[prev_c] += int(c)
        elif c in '()[]{}':
            pass

    return out_dict

print(parse_molecule("H2O"))# {'H': 2, 'O' : 1}
print(parse_molecule("H2O2IL3M"))# {'H': 2, 'O' : 1}



# test.assert_equals(parse_molecule("H2O"), {'H': 2, 'O' : 1}, "Should parse water")
# test.assert_equals(parse_molecule("Mg(OH)2"), {'Mg': 1, 'O' : 2, 'H': 2}, "Should parse magnesium hydroxide: Mg(OH)2")
# test.assert_equals(parse_molecule("K4[ON(SO3)2]2"), {'K': 4,  'O': 14,  'N': 2,  'S': 4}, "Should parse Fremy's salt: K4[ON(SO3)2]2")