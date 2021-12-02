def spin_words(sentence):
    words = sentence.split()
    output = []
    for x in words:
        if len(x) > 4:
            output.append(x[::-1])
        else:
            output.append(x)
    return ' '.join(output)


print(spin_words("Welcome to the end"))