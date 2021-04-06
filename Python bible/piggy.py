# get sentence

original = input("Sentence here: ").strip().lower()

# split into words

words = original.split()

# loop and convert to pig latin

new_words = []

for word in words:
    if word[0] in "aeiou"
        new_word = word + "yay"
        new_words.append(new_word)
    else:
        vowel_position = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_position = vowel_position + 1
            else;
            break
        cons = word[:vowel_position]
        the_rest = word[vowel_position:]
        new_word = the_rest + consonants + "ay"
        new_words.append(new_word)

# Join words

converted = " ".join(new_words)
print(converted)
