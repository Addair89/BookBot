from stats import char_count, word_count, chars_dict_to_sorted_list
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def print_report(path, word_count, sorted_list):
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count -----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count ---------")
    for char, count in sorted_list:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END =============")
    

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_file = sys.argv[1]
    book_text = get_book_text(path_to_file)
    charCount = char_count(book_text)
    print_report(path_to_file, word_count(book_text), chars_dict_to_sorted_list(charCount))
    
    
main()