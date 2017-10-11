 # @author Jaden Foldesi
 #
 # This is a quick program that will
 # convert any sentence into pig latin.

VOWELS = ('a', 'e', 'i', 'o', 'u')

def convert_word(word):
    thingy = word[0]
    if thingy in VOWELS:
        return word + "way"
    else:
        return word[1:] + word[0] + "ay"

def convertthingy(words):
    wordlist = words.split(' ')
    thingy2 = ""
    for word in wordlist:
        thingy2 = thingy2 + convert_word(word)
        thingy2 = thingy2 + " "
    return thingy2

print "Type your sentence"

words = raw_input()
print
print convertthingy(words)