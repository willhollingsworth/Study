def anagrams(word, w_list):
    out_list = []
    for current_word in w_list:
        temp_word = word
        for char in current_word:
            if char in temp_word:
                temp_word = temp_word.replace(char,'',1)
            else:
                break
            if len(temp_word) == 0 and len(current_word) == len(word):
                out_list.append(current_word)
    return out_list





print(anagrams('abba', ['aabb', 'abcd']))
print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])
print(anagrams('abba',['aabb', 'bbaa', 'abab', 'baba', 'baab', 'abbab', 'abbaa', 'babaa']),['aabb', 'bbaa', 'abab', 'baba', 'baab']) 
# ['aabb', 'bbaa', 'abab', 'baba', 'baab', 'abbab', 'abbaa', 'babaa'] should equal ['aabb', 'bbaa', 'abab', 'baba', 'baab']

#   target_list = list(word)
#         current_list = list(current_word)
#         for x in range(len(target_list)):
#             target_letter = target_list[x]
#             if target_letter in current_list:
#                 current_list.remove(target_letter)
#                 target_list.remove(target_letter)


#             for letter in target_list:
#                 if letter in current_word:
#                     target_list.remove(letter)
#                     print('removed')
#                 else:
#                     print('not removed')
#                     break


#         for y in x:
#             if y in word:
#                 current_word.remove(y)
#             else:break
#         out_list.append(x)