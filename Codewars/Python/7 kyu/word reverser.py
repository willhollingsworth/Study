# Stop gninnipS My sdroW!
def spinWords(in_string):
    word_list = in_string.split()
    working_list = []
    for x in word_list:
        if len(x) > 4:
            working_list.append(x[::-1])
        else:
            working_list.append(x)
    return ' '.join(working_list)
    

print(spinWords( "Hey fellow warriors" ),"Hey wollef sroirraw")
print(spinWords( "This is a test"),"This is a test")
print(spinWords( "This is another test" ),"This is rehtona test")