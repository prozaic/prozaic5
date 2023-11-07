import nltk
from nltk.corpus import wordnet
import sys

nltk.download('wordnet')

def get_word_definitions(word):
    synsets = wordnet.synsets(word)
    if not synsets:
        return f"No definitions found for '{word}'."

    definitions = []
    for synset in synsets:
        definitions.append(f"{synset.name()}: {synset.definition()}")

    return '\n'.join(definitions)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 pythondefinition.py <word>")
        sys.exit(1)

    word = sys.argv[1]
    definitions = get_word_definitions(word)
    print(definitions)
