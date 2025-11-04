import string
from operator import itemgetter


def reader(filename):
    dictionary = {}
    with open(filename) as f:
        sentence = f.read().lower()
        sentence = sentence.translate(str.maketrans("", "", string.punctuation))
        words = sentence.split()
        for word in words:
            dictionary[word] = dictionary.get(word, 0) + 1
        return dictionary


def print_words(filename):
    print("\nPrinting all words")
    dictionary = reader(filename)
    for word, count in sorted(dictionary.items()):
        print(word, count)


def print_top(filename):
    print("\nPrinting top 20 most common words")
    dictionary = reader(filename)
    new_dictionary = sorted(dictionary.items(), key=itemgetter(1), reverse=True)
    for word, count in new_dictionary[:20]:
        print(word, count)


def main():
    print("=== Word Count Program ===")
    print_words("small.txt")
    print()
    print_top("alice.txt")


if __name__ == "__main__":
    main()
