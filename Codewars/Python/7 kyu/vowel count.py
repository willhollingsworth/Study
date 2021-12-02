def get_count(sentence):
    count = 0
    vowels = 'aeiou'
    for x in sentence:
        if x in vowels:
            count +=1
    return count



print(get_count('aeiou'))