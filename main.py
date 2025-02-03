def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    alphabet = char_counter(text)
    alph = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i in alph:
            print(f"The '{i}' character was found {alphabet[i]} times")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def char_counter(text):
    characters = {}
    for char in text.lower():
        characters[char] = characters.get(char, 0) + 1
    return characters



main()