def words_count(text):
    return len(text.split())

with open('books/frankenstein.txt') as f:
    file_contents = f.read()
    #print(file_contents)
    wc = words_count(file_contents)
    print(f'Word Count: {wc}')

