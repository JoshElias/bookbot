def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    wc = get_word_count(text)
    print("Book Word Count: ", wc)
    cc = get_chars_dict(text)
    print("Book Char Counts: ", cc)

def get_word_count(text):
    return len(text.split())

def get_book_text(path): 
    with open(path) as f:
        return f.read()

def get_chars_dict(text):
    word_counts = {}
    for c in text:
        c = c.lower()
        if not c in word_counts:
            word_counts[c] = 0
        word_counts[c] += 1
    return word_counts

main()
