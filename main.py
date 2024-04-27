def main():
    book_path = 'books/frankenstein.txt'
    text = get_book_text(book_path)
    wc = get_word_count(text)
    print("Book Word Count: ", wc)

def get_word_count(text):
    return len(text.split())

def get_book_text(path): 
    with open(path) as f:
        return f.read()

main()
