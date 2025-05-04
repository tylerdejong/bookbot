def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return words

def get_char_counts(text):  

    character_dict = {}
    for c in text.lower():
        if c in character_dict:
            character_dict[c] += 1
        else:
            character_dict[c] = 1
    return character_dict

def get_sorted(char_dict):
    char_list = []
    for char, count in char_dict.items():
        char_list.append({"char": char, "num": count})
    char_list.sort(key=lambda item: item["num"], reverse=True)
    return char_list
