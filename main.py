from stats import count_words
from stats import count_characters



book = "/Users/bg/Code/bookbot/books/frankenstein.txt"

    
def get_book_text():
    with open(book) as f:
        return f.read()

def main():
    text = get_book_text()
    counts = count_characters(text)
    print(f"Found {count_words(text)} total words")
    print(counts)
       
if __name__ == "__main__":
    main()