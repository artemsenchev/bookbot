
def get_num_words(book):
    words = book.split()
    return len(words)

def get_count_characters(book):
    book = book.lower()
    uniques = set(book)
    

    count_dict = {}
    for char in uniques:
        count_dict[char] = book.count(char)

    return count_dict

def sort_dict(count_dict):
    sorted_dict = dict(sorted(count_dict.items(), key=lambda item: item[1],reverse=True))
    return sorted_dict

