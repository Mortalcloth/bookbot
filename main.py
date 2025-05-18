from stats import count_words
from stats import count_characters
from stats import get_book_text

def main(the):
    word_count = count_words(the)
    letter_count = count_characters(get_book_text(the))
    

main("books/frankenstein.txt")