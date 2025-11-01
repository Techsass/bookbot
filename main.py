import sys
from stats import count_words, count_chars, sort_chars

def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = count_words(text)
    char_count = count_chars(text)
    sorted = sort_chars(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(num_words)
    print("--------- Character Count -------")
    for char in sorted:
        if char["char"].isalpha() == False:
            continue
        else:
            print(f"{char['char']}: {char['count']}")

if __name__ == "__main__":
    main()