from stats import word_count
from stats import letter_count
from stats import sort_letter_freq
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        booktext = f.read()
        return booktext
    
    

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    book = get_book_text(sys.argv[1])
    print(f"Analyzing book found at {sys.argv[1]}")
    # print(book)
    print("----------- Word Count ----------")
    word_count(book)
    print("--------- Character Count -------")
    letters_dict = letter_count(book)
    # print(letters_dict)
    sorted_list = sort_letter_freq(letters_dict)
    
    for dict in sorted_list:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")
main()