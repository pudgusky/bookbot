book_path = "books/frankenstein.txt"
book_contents = open(book_path).read()
letters = 'abcdefghijklmnopqrstuvwxyz'


def main():
    print('some summarzied info about Frankenstein the book')
    print(f'{word_count(book_contents)} words are in the book')
    book_letters = character_count(book_contents)
    sorted_book_letters = sorted_dict_by_values_desc(book_letters)
    for letter, count in sorted_book_letters.items():
        print(f'{letter} is found {count} times in the book')
    return


def word_count(text):
    return len(text.split())


def character_count(text):
    text = text.lower()
    character_dict = {}
    for i in letters:
        character_dict[i] = text.count(i)
        #print(f'{i} is found {character_dict[i]} times in the text')
    return character_dict


def sorted_dict_by_values_desc(dictionary):
    return dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))

main()
