def print_upper_words(words):
    """Print each word on sep line, uppercased.

        >>> print_upper_words(["I", "saw", "an", "elephant", "at", "the", "zoo"])
        I   
        SAW
        AN
        ELEPHANT
        AT
        THE
        ZOO
    """
    
    for word in words:
            print (word.upper())

print_upper_words(["I", "saw", "an", "elephant", "at", "the", "zoo"])


def print_upper_words2(words):
    """Print each word on sep line, uppercased, if starts with E or e.

        >>> print_upper_words2(["Everyday", "I", "see", "an", "elephant", "at", "the", "zoo"])
        EVERYDAY
        ELEPHANT
    """
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print (word.upper())

print_upper_words2(["Everyday", "I", "see", "an", "elephant", "at", "the", "zoo"])


def print_upper_words3(words, must_start_with):
    """Print each word on sep line, uppercased, if starts with one of given letters

        >>> print_upper_words3(["hello", "hey", "goodbye", "yo", "yes"],
        ...                   must_start_with=["h", "y"])
        EDWARD
        ALFRED
    """
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break

print_upper_words3(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})

