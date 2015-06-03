def is_palindrome(word):
    return word == word[::-1]


def palindromes():
    word = input('Enter word>')
    word_length = len(word)
    word += word
    palindromes = set()
    for start in range(word_length):
        end = start+word_length
        next_rotation = word[start:end]
        if is_palindrome(next_rotation) and next_rotation not in palindromes:
            palindromes.add(next_rotation)
            print(next_rotation)
