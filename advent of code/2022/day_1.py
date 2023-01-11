import day1_input
input = day1_input.input

elfs = input.split('\n\n')
elfs = [elf.split('\n') for elf in elfs]
elf_total = []
for elf in elfs:
    temp = 0
    for item in elf:
        if not item == '':
            temp += int(item)
    elf_total.append(temp)
elf_total.sort()
print('day1',elf_total[-1])
print('day1 part 2:',elf_total[-3:])
print('day1 part 2:',sum(elf_total[-3:]))