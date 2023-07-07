# https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python



# brute force approach
def strip_comments(str, markers):
    output = ''
    skipping = False
    whitespace = [' ','\t']
    for i,s in enumerate(str):
        if s in markers : skipping = True
        if not skipping :
            if s in whitespace:
                offset = i
                while not skipping:
                    offset += 1
                    if str[offset] in whitespace : continue
                    elif str[offset] in markers+['/n'] : skipping = True
                    else : 
                        output +=s
                        break
            else:
                output +=s
        elif skipping:
            if s == '\n':
                output +=s
                skipping = False
    return output

# top solution
# def strip_comments(str, markers):
#     lines = str.splitlines()
#     for m in markers:
#         lines = [l.split(m)[0].rstrip() for l in lines]
#     return '\n'.join(lines)

print('abcd'.index('c'))

# strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!'])
# print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']),'\n' ,'apples, pears\ngrapes\nbananas')
# print(strip_comments('a #b\nc\nd $e f g', ['#', '$']), 'a\nc\nd')
# print(strip_comments(' a #b\nc\nd $e f g', ['#', '$']), ' a\nc\nd')