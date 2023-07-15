def pig_it(text):
    punctuation = '!?'
    words = [w[1:]+w[0]+'ay' if w not in punctuation else w 
                for w in text.split()]
    return ' '.join(words)
# print(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')
# print(pig_it('This is my string'),'hisTay siay ymay tringsay')
print(pig_it('O tempora o mores !'))