# Word counter

input_string = "Hello Ryan Josh said hello"
words = input_string.lower().split()
print(words)

# word_count = {}
# for word in words:
#     if word in word_count:
#         word_count[word] += 1
#     else: 
#         word_count[word] = 1

# print(word_count)


counter = 0
for i in words:
    if i:
        counter += 1

    print(counter) 