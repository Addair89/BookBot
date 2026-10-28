def word_count(text):
    words = text.split()
    return len(words)

def char_count(text):
    charDict = {}
    for char in text:
        if char.lower() not in charDict:
            charDict[char.lower()] = 1
        else:
            charDict[char.lower()] += 1
    return charDict

def sort_on(character: tuple[str, int]):
    return character[1]

def chars_dict_to_sorted_list(charDict: dict[str, int]):
    list_counts = []
    for char, count in charDict.items():
        list_counts.append((char, count))
    sorted_list = sorted(list_counts, reverse=True, key=sort_on)
    return sorted_list