import re

def main():
    book = "books/frankenstein.txt"
    with open(book) as f:
        contents = f.read()

    word_count = count_words(contents)
    char_dict = count_chars(contents)   
    
    print(f"--- Begin report of {book} ---")
    print(f"{word_count} words found in the document")
    print()
    # iterate every character
    for char in char_dict:
        print(f"The '{char}' character was found {char_dict[char]} times")
    print("--- End report ---")

def count_words(text):
    return len(text.split())

def count_chars(text):
    dict = {}
    
    cleaned_text = re.sub(r'[^a-zA-Z]', '', text)
    for char in cleaned_text.lower():
        if char in dict.keys():
            dict[char] += 1
        else:
            dict[char] = 1

    return dict
main()
