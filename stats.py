def count_words(text):
    countable = text.split()
    count = 0
    for word in countable:
        count += 1
    return f"Found {count} total words"

def count_chars(text):
    char_count_dict = {}
    lower_text = text.lower()
    for char in lower_text:
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    return char_count_dict

def sort_on(items):
    return items["count"]

def sort_chars(char_dict):
    char_count_list = []
    for char_count in char_dict:
        char_count_list.append({"char": char_count, "count": char_dict[char_count]})
    char_count_list.sort(reverse=True, key=sort_on)
    return char_count_list 
    