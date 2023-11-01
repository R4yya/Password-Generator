from secrets import choice
from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def generate_secure_password(length, uppercase_statement=True, digits_statement=True, punctuation_statement=True):
    alphabet = ascii_lowercase

    alphabet += ascii_uppercase if uppercase_statement else ''
    alphabet += digits if digits_statement else ''
    alphabet += punctuation if punctuation_statement else ''

    password = ''.join(choice(alphabet) for _ in range(length))

    return password


if __name__ == '__main__':
    secure_password = generate_secure_password(12)
    print(secure_password)
