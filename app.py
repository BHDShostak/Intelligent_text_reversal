def reverse_words(sentence: str) -> [str]:
    words = sentence.split()
    reversed_raw_symbols = []


    for word in words:
        reversed_raw_symbols.append(reverse_word(word))

    return ' '.join(reversed_raw_symbols)


def reverse_word(word: str) -> str:
    reversed_raw_word = []
    alpha_word = [symbol for symbol in word if symbol.isalpha()]

    for symbol in word:

        if symbol.isalpha():

            reversed_raw_word.append(alpha_word.pop())
        else:
            reversed_raw_word.append(symbol)

    return ''.join(reversed_raw_word)


if __name__ == '__main__':
    cases = [
        ('abcd efgh', 'dcba hgfe'),
        ('a1bcd efg!h', 'd1cba hgf!e'),
        ('', '')
    ]
    for sentence, reversed_sentence in cases:
        assert reverse_words(sentence) == reversed_sentence