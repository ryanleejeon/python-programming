
vowel = "aeiou"
word = "cattle"

# def vowel_detect(word, vowel):
#     detected = []
#     for c in word:
#         if c in vowel:
#             detected.append(c)
#         else: 
#             print("not a vowel")
        
#     return detected

# result = vowel_detect(word,vowel)
# print(result)

vowel_dict = {}

for c in word:
    if c in vowel:
        if c in vowel_dict:
            vowel_dict[c] += 1
        else: 
            vowel_dict[c] = 1



vowel_dict = {}
for c in word:
    if c in vowel_dict:
        vowel_dict[c] += 1
    else:
        vowel_dict[c] = 1

print(vowel_dict)








