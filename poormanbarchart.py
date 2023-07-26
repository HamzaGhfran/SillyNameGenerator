"""Generate simple Bar chart graph of letter"""
import pprint as pp
from collections import defaultdict
def main():
    """using defaultdict method to build dictionary"""
    mapped = defaultdict(list)
    sentence = "my name is hamza ghafran"
    for word in sentence:
        if word.isalpha():
            mapped[word].append(word)

    pp.pprint(mapped, width=110)

if __name__ == "__main__":
    main()