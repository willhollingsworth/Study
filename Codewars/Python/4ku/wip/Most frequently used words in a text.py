from collections import Counter
import re

def top_3_words(text):
    # strip non alphas + ' , only return words contains alphas
    text = [re.sub('[^a-z\'0-9]','',w.lower()) for w in text.split() if re.findall('\w',w)]
    output = [l[0] for l in Counter(text).most_common(3)]
    return output

print(top_3_words("a a a  b  c c  d d d d  e e e e e"), ["e", "d", "a"])
print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])
print(top_3_words("  //wont won't won't "), ["won't", "wont"])
print(top_3_words("  , e   .. "), ["e"])
print(top_3_words("  ...  "), [])
print(top_3_words("  '  "), [])
print(top_3_words("  '''  "), [])
print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
#         mind, there lived not long since one of those gentlemen that keep a lance
#         in the lance-rack, an old buckler, a lean hack, and a greyhound for
#         coursing. An olla of rather more beef than mutton, a salad on most
#         nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
#         on Sundays, made away with three-quarters of his income."""), ["a", "of", "on"])