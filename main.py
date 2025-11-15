from stats import count_words


book = "/home/boot/bookbot/books/frankenstein.txt"

    
def get_book_text():
    with open(book) as f:
        return f.read()

def main():
    text = get_book_text()
    print(f"Found {count_words(text)} total words")
       
if __name__ == "__main__":
    main()