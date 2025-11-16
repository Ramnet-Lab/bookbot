characters = set()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text = text.lower()
    counts = {}
    for character in text:
        if character in counts:
            counts[character] += 1 
        else:
            counts[character] = 1
    return counts

def sorted_list_of_dicts(counts):
    character_list = []
    for character, count in counts.items():
        character_list.append({"char": character, "num": count})
    def get_num(item):
        return item["num"]
    character_list.sort(key=get_num, reverse=True)
    return character_list
    
    
