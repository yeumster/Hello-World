def piglatin(sentence):
    a = sentence.lower().split()
    b = " "
    c = []
    vowels = ["a", "e", "i", "o", "u"]
    punctuation = [".", ",", "!", "?", ":", "(", ")", "-", "'", "\"", "\\"]
    for word in a:
        word.strip()
        punc = ""
        # Strips punctuation from end of word and stores it
        if word[len(word) - 1] in punctuation:
            punc = word[len(word) - 1]
            word = word[:len(word) - 1]
        pigword = ""
        # If word starts with a vowel, append "yay"
        if word[0] in vowels:
            pigword = word + "yay"
        elif word[0] is "y":
            pigword = word[1:] + "yay"
        # If starts with consonants, apply pig latin
        else:
            i = 0
            end = ""
            while word[i] not in vowels and word[i] is not "y":
                end += word[i]
                i += 1
            pigword = word[i:] + end + "ay"
        c.append(pigword + punc)
    b = b.join(c)
    return b

sentence = input("Input a sentence (Write \"stop\" to stop): ")
while sentence != 'stop':
    print(piglatin(sentence))
    sentence = input("Input a sentence: ")
