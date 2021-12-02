def duplicate_count(text):
    text = text.lower()
    checked = ''
    uniques = 0
    for x in text:
        if text.count(x) > 1:
            if x not in checked:
                uniques += 1
                checked += x
    return uniques

print(duplicate_count(""), 0)
print(duplicate_count("abcde"), 0)
print(duplicate_count("abcdeaa"), 1)
print(duplicate_count("abcdeaB"), 2)
print(duplicate_count("Indivisibilities"), 2)