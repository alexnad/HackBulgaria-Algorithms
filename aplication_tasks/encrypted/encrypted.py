import itertools


def extract_elements(encrypted):
    elements = {}
    middle = len(encrypted)//2
    encrypted = encrypted[middle:] + encrypted[:middle]
    alphabet_begining = encrypted.find('~')+1
    alphabet_length = int(encrypted[:alphabet_begining-1])
    alphabet_end = alphabet_begining + alphabet_length
    elements['alphabet'] = encrypted[alphabet_begining:alphabet_end]
    key_end = - (encrypted[::-1].find('~')+1)
    key_length = int(encrypted[key_end+1:])
    key_begining = key_end - key_length
    elements['key'] = encrypted[key_begining:key_end]
    elements['message'] = encrypted[alphabet_end:key_begining]
    return elements


def key_generator(key):
    for char in itertools.cycle(key):
        yield char


def decrypt():
    encrypted = input('Enter your message>')
    elements = extract_elements(encrypted)
    key = key_generator(elements['key'])
    decrypted = ''
    alphabet = elements['alphabet']
    length = len(alphabet)
    for symbol in elements['message']:
        actual_symbol = alphabet.find(symbol) - alphabet.find(key.__next__())
        if actual_symbol < 0:
            actual_symbol = length + actual_symbol
        decrypted += alphabet[actual_symbol]

    print(decrypted)
