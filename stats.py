def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    char_counts = {}

    for char in text.lower():
        char_counts[char] = char_counts.get(char, 0) + 1

    return char_counts

def get_sorted_char_list(char_counts):
    # Convert dictionary to list of dictionaries
    char_list = []
    for char, count in char_counts.items():
        char_list.append({"char": char, "num": count})

    # Sort by count (highest to lowest)
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def sort_on(item):
    return item["num"]
