# def to_camel_case(text):
#     if text == '' : return ''
#     words = re.split('_|-',text)
#     words = [words[0]] + [ word[0].upper()+word[1:] for word in words[1:]]
#     return ''.join(words)

def to_camel_case(text):
    if text == '' : return ''
    output = text.title().replace('-',' ').replace('_',' ').split()
    return text[0]+''.join(output)[1:]






# print(to_camel_case(""), "")
print(to_camel_case("the_stealth_warrior"), "theStealthWarrior")
# print(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior")
# print(to_camel_case("A-B-C"), "ABC",)
# print(to_camel_case("A_Pippi-Was-Savage"))


