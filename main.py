def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    #wc = get_word_count(text)
    cc = get_chars_dict(text)
    sorted_char_data = get_char_counts_sorted(cc)
    print_char_report(sorted_char_data)


def get_word_count(text):
    return len(text.split())

def get_book_text(path): 
    with open(path) as f:
        return f.read()

def get_chars_dict(text):
    word_counts = {}
    for c in text:
        if not c.isalpha():
            continue
        c = c.lower()
        if not c in word_counts:
            word_counts[c] = 0
        word_counts[c] += 1
    return word_counts

def sort_on(dict):
    return dict['count']

def get_char_counts_sorted(char_dict):
    char_objects = []
    for k in char_dict:
        char_obj = {}
        char_obj['name'] = k
        char_obj['count'] = char_dict[k]
        char_objects.append(char_obj)
    char_objects.sort(reverse=True, key=sort_on)
    return char_objects

def print_char_report(char_data_sorted):
    for v in char_data_sorted:
        print(f"The '{v["name"]}' character was found {v["count"]} times")

main()
