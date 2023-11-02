from secrets import choice
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def generate_secure_password(length, uppercase_statement=True, digits_statement=True, punctuation_statement=True):
    alphabet = ascii_lowercase

    alphabet += ascii_uppercase if uppercase_statement else ''
    alphabet += digits if digits_statement else ''
    alphabet += punctuation if punctuation_statement else ''

    password = ''.join(choice(alphabet) for _ in range(length))

    return password


def generate_mnemonic_password(password):
    letter_to_words = {
        'a': ['apple', 'apartment', 'awesome', 'amazing', 'ate'],
        'b': ['banana', 'ball', 'beach', 'bird', 'book'],
        'c': ['cat', 'car', 'cake', 'chocolate', 'cloud'],
        'd': ['dog', 'desk', 'dolphin', 'diamond', 'dream'],
        'e': ['elephant', 'egg', 'earth', 'energy', 'enjoy'],
        'f': ['fox', 'flower', 'forest', 'fire', 'friend'],
        'g': ['giraffe', 'game', 'guitar', 'grass', 'green'],
        'h': ['horse', 'hat', 'house', 'heart', 'happy'],
        'i': ['ice cream', 'island', 'igloo', 'insect', 'imagine'],
        'j': ['jellyfish', 'jacket', 'juice', 'jungle', 'joy'],
        'k': ['kangaroo', 'kite', 'key', 'king', 'kind'],
        'l': ['lion', 'lamp', 'lake', 'leaf', 'laugh'],
        'm': ['monkey', 'moon', 'mountain', 'music', 'magic'],
        'n': ['nose', 'net', 'nest', 'night', 'new'],
        'o': ['octopus', 'owl', 'ocean', 'orange', 'open'],
        'p': ['panda', 'pear', 'piano', 'penguin', 'peace'],
        'q': ['queen', 'quill', 'quiet', 'quilt', 'question'],
        'r': ['rabbit', 'rose', 'rainbow', 'robot', 'run'],
        's': ['sun', 'star', 'sea', 'snow', 'smile'],
        't': ['tiger', 'tree', 'train', 'turtle', 'top'],
        'u': ['unicorn', 'umbrella', 'up', 'unique', 'under'],
        'v': ['volcano', 'violin', 'vase', 'violet', 'village'],
        'w': ['whale', 'water', 'wind', 'wonder', 'wish'],
        'x': ['xylophone', 'x-ray', 'xenon', 'xylitol', 'xenophobia'],
        'y': ['yak', 'yogurt', 'yellow', 'year', 'youth'],
        'z': ['zebra', 'zipper', 'zero', 'zeppelin', 'zucchini']
    }

    mnemonic_password = ''
    letter_index = 0

    for char in password:
        if char.isalpha():
            letter = char.lower()
            if letter in letter_to_words:
                word_list = letter_to_words[letter]
                if word_list:
                    word = word_list[letter_index % len(word_list)]
                    letter_index += 1
                    mnemonic_password += word if char.islower() else word.capitalize()
                else:
                    mnemonic_password += char
            else:
                mnemonic_password += char
        else:
            mnemonic_password += char

    return mnemonic_password


if __name__ == '__main__':
    secure_password = generate_secure_password(6)
    print(f'Your generated password {secure_password}')

    mnemonic_password = generate_mnemonic_password(secure_password)
    print(f'Your mnemonic password {mnemonic_password}')
