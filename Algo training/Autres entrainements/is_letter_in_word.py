# Ce programme vise à déterminer si une lettre parmis une liste donnée (letters) est présente dans un ou plusieurs mots d'une liste (words)

# Transforme une chaine de charactères "abcd" en une liste des lettres ["a","b","c","d"]
# Arguments :
# letters : string
# retourne :
# - letter_list : array of chars

def get_letters(letters):
    letter_list = []
    for letter in letters :
        if letter in letter_list :
            continue
        else :
            letter_list.append(letter)
    return letter_list

# Détermine si un ou des mots parmis les "words" contiennent une lettre parmis "letters"
#
# Arguments :
# - words : array of string
# - letters : string
# retourne :
# - word_list : array of string

def which_words_have_letters(words,letters):
    word_list = []
    for word in words :
        for letter in letters :
            if letter in word :
                if word in word_list:
                    continue
                else :
                    word_list.append(word)
    return word_list

print(which_words_have_letters(["bonjour","merci","adieu","zoo","camembert","oooottt","piri piri"],get_letters("aftb")))