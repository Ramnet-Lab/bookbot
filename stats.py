characters = set()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    counts = {}
    for characters in text:
        if characters in counts:
            counts[characters] += 1 
        else:
            counts[characters] = 1

    return counts