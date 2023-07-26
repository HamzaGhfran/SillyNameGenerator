"""Generate poor forign man bar chart"""
import pprint as pp
from collections import defaultdict
from googletrans import Translator
def main():
    """using defaultdict method to build dictionary"""
    translator = Translator()
    mapped = defaultdict(list)
    sentence = "Borra con el codo lo que escribe con la mano."
    sentence = translator.translate(sentence)
    print(sentence)
    for word in sentence.text:
        if word.isalpha():
            mapped[word].append(word)

    pp.pprint(mapped, width=110)
if __name__ == "__main__":
    main()