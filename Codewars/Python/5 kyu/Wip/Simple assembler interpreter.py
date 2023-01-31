import codewars_test as test



def simple_assembler(program):
    out_dict = {}
    instructions = list(zip(range(len(program)),program))
    print(instructions)
    target = 0
    while True:
        if target >= len(instructions):
            break
        split_line = instructions[target][1].split(' ')
        instruction = split_line[0]
        variable = split_line[1]
        value = None
        if len(split_line) > 2:
            try:
                value = int(split_line[2])
            except:
                value = out_dict[split_line[2]]
        # print(target,instruction,variable,value)
        if not variable in out_dict.keys():
            if not any([chr for chr in variable if chr.isdigit()]):
                out_dict[variable] = 0
        if instruction == 'mov':
            out_dict[variable] = value
        elif instruction == 'inc':
            out_dict[variable] = out_dict[variable] + 1
        elif instruction == 'dec':
            out_dict[variable] = out_dict[variable] - 1
        elif instruction == 'jnz':
            
            jnz_variable = out_dict[variable]
            if not any([chr for chr in jnz_variable if chr.isdigit()]):
                if out_dict[variable] != 0:
                    target += value-1
        # return a dictionary with the registers
        # print(out_dict)
        target += 1 
    print(out_dict)
    return out_dict

code = '''\
mov c 12
mov b 0
mov a 200
dec a
inc b
jnz a -2
dec c
mov a b
jnz c -5
jnz 0 1
mov c a'''
simple_assembler(code.splitlines())


# @test.describe("Sample tests")
# def _():
#     @test.it("Tests")
#     def __():
#         code = '''\
# mov a 5
# inc a
# dec a
# dec a
# jnz a -1
# inc a'''
#         test.assert_equals(simple_assembler(code.splitlines()), {'a': 1})

#         code = '''\
# mov c 12
# mov b 0
# mov a 200
# dec a
# inc b
# jnz a -2
# dec c
# mov a b
# jnz c -5
# jnz 0 1
# mov c a'''
#         test.assert_equals(simple_assembler(code.splitlines()), {'a': 409600, 'c': 409600, 'b': 409600})