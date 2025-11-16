from stats import count_words
from stats import count_characters
from stats import sorted_list_of_dicts
import sys


if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book = sys.argv[1]
   
def get_book_text():
    with open(book) as f:
        return f.read()

def main():
    text = get_book_text()
    counts = count_characters(text)
    report = sorted_list_of_dicts(counts)
    print (f"============ BOOKBOT ============\nAnalyzing book found at {book}...\n----------- Word Count ----------")
    print(f"Found {count_words(text)} total words")
    # print(counts)
    print ("--------- Character Count -------")
    for item in report:
        ch = item["char"]
        num = item["num"]
        if ch.isalpha():                         # only print letters
            print(f"{ch}: {num}")
    print("============= END ===============")
       
if __name__ == "__main__":
    main()