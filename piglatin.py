"""Generate pig-latin word"""
import sys
def main():
    """Checking first character is vowel or consonant"""
    vowel = "aeiou"
    while True:
        word = input("Type a word to ge pig-latin string!: ")
        if word[0] in vowel:
            pig_latin = word + "way"
        else:
            pig_latin = word[1:] + word[0] + "ay"
        print(pig_latin)
        try_again = input("\n\nTry again (Press ENTER or n to stop!)")
        if try_again.lower() == "n":
            sys.exit()
if __name__ == "__main__":
    main()