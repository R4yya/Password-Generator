from math import log2
from re import search
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def calculate_entropy(password):
    alphabet_size = 0

    if search(r'[a-z]', password):
        alphabet_size += len(ascii_lowercase)
    if search(r'[A-Z]', password):
        alphabet_size += len(ascii_uppercase)
    if search(r'[\d]', password):
        alphabet_size += len(digits)
    if search(f'[{punctuation}]', password):
        alphabet_size += len(punctuation)

    password_length = len(password)

    return log2(alphabet_size ** password_length)


def evaluate_password_strength(entropy):
    if entropy < 28:
        return "very weak"
    elif entropy < 36:
        return "weak"
    elif entropy < 60:
        return "moderate"
    elif entropy < 128:
        return "strong"
    else:
        return "very strong"


if __name__ == '__main__':
    password_entropy = calculate_entropy(input('Password: '))
    password_strength = evaluate_password_strength(password_entropy)

    print(f'Password entropy: {password_entropy} bits')
    print(f'This password is {password_strength}')
