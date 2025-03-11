import os
from stats import get_num_words
from stats import get_count_characters
from stats import sort_dict
import sys

def get_book_text(path_to_file):
    with open(path_to_file, 'r', encoding='utf-8') as f:
        book = f.read()
    return book


def main():

    input = sys.argv
    if len(input) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    relative_path = input[1]

    current_directory = os.getcwd()
 
    path_to_file = os.path.join(current_directory, relative_path)

    try:
        book = get_book_text(path_to_file)
    except FileNotFoundError:
        print(f"file {path_to_file} not found")
        return
 
    num_words = get_num_words(book)
    
    count_dict = get_count_characters(book)
    sorted_dict = sort_dict(count_dict)
 
    

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {relative_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("---------- Character Count -------")
    for key, value in sorted_dict.items():
        print(f"{key}: {value}")
    print("============= END ===============")

    


main()