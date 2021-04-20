def is_pangram(sentence):
    sentence = sentence.lower()
    letters = ''.join([i for i in sentence if i.isalpha()])
    remove_dups = ''.join(set(letters))

    return len(remove_dups) == 26





