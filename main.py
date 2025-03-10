import sys

from stats import get_num_words, char_count, sorted_chars

def get_book_text(url):
    with open(url) as f:
        file_contents = f.read()
    return file_contents

def main():
    try:
        url = sys.argv[1]
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1) 
    bt = get_book_text(url)
    header = "============ BOOKBOT ============"
    print(header)
    print(f"Analyzing book found at {url}...")
    print("----------- Word Count ----------")
    print(get_num_words(bt))
    print("--------- Character Count -------")
    #print(char_count(bt))
    for i in sorted_chars(char_count(bt)):
        for k in i:
            print(f"{k}: {i[k]}")
    print("============= END ===============")
    return 0

main()