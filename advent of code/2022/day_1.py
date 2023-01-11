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
print(elf_total[-1])

