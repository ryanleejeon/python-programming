# Check if a word is a palidrome

word = "lols"


def palidrome(word):
    reverse = word[::-1]
    return word == reverse

if palidrome(word):
    print("This is a palidrome")
else: 
    print("not a palidrome")