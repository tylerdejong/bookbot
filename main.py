import sys

from stats import get_book_text, get_num_words, get_char_counts, get_sorted

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    word_count = get_num_words(text)
    char_counts = get_char_counts(text)
    sorted_chars = get_sorted(char_counts)

    ## REPORT ##
    print("============ BOOKBOT ============")
    print("Analyzing book found at", path)
    print("----------- Word Count ----------")
    print("Found", len(word_count), "total words")
    print("--------- Character Count -------")
    
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["num"]
        #print alpha characters only
        if char.isalpha():
            print (f"{char}: {count}")
    

main()

   # "/Users/tylerdejong/workspace/github.com/tylerdejong/bookbot/books/frankenstein.txt"               