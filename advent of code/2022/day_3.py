import os,string
os.chdir(os.path.dirname(os.path.realpath(__file__))) # force file paths to be local to script exec folder
input = open('inputs\\day3.txt','r').readlines()
# input = [
# 'vJrwpWtwJgWrhcsFMMfFFhFp', 
# 'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
# 'PmmdzqPrVvPwwTWBwg',
# 'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
# 'ttgJtRGJQctTZtZT',
# 'CrZsJsPPZsGzwwsLwLmpwMDw',
# ]

p = string.ascii_lowercase + string.ascii_uppercase # priorities 


# strip new lines chars
for line in range(len(input)): 
    input[line] = input[line].replace('\n','')

# find all duplicates between the two compartments
shared_letters = []
priority_total = 0
for c in input:
    matches = ''
    l = len(c)
    first = c[l//2:]
    second = c[:l//2]
    for item in first:
        if item in second and not item in matches:
            matches += item
            priority_total += p.find(item) + 1
    shared_letters.append(matches)




print(len(input))
print(shared_letters)

print('part1:',priority_total)