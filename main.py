from io import StringIO
def main():
    BOOK_PATH = "books/frankenstein.txt"
    with open(BOOK_PATH) as f:
        text = f.read()
        print(get_report(BOOK_PATH, text))

def count_words(text):
    return len(text.split())

def count_chars(text):
    char_dict = {}
    for char in text:
        char = char.lower()
        if not char in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def get_report(name, text):
    num_words = count_words(text)
    char_dict = count_chars(text)
    reportStream = StringIO()
    reportStream.write(f"--- Begin reportStream of {name} ---\n")
    reportStream.write(f"{num_words} words found in the document\n\n")

    for char, freq in char_dict.items():
        if char.isalpha():
            reportStream.write(f"The '{char}' character was found {freq} times\n")
    reportStream.write("--- End report ---\n")
    report = reportStream.getvalue()
    reportStream.close()
    return report


if __name__ == '__main__':
    main()