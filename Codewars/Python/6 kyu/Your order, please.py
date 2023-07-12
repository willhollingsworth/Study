# https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python

def order(sentence) -> str:
    words = sentence.split()
    output = words.copy()
    for word in words:
        index = int(''.join([c for c in word if  c.isdigit()]))-1
        output[index] = word
    return ' '.join(output)


print(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
print(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
print(order(""), "")