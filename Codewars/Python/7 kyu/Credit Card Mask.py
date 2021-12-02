'''
https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python
Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.

Examples
maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""

# "What was the name of your first pet?"
maskify("Skippy")                                   == "##ippy"
maskify("Nananananananananananananananana Batman!") == "####################################man!"
'''


# return masked string
def maskify(cc):
    if len(cc) <= 4:
        return cc
    end = cc[-4:]
    hash_count = len(cc)-4
    return '#'*hash_count+end



print(maskify("SF$SDfgsd2eA"))
print(maskify("Skippy"))
print(maskify("red1"))
print(maskify("123456789"))
print(maskify("12"))