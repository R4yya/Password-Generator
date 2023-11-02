from secrets import choice
from string import ascii_lowercase, ascii_uppercase, digits, punctuation
import nltk
from nltk.corpus import words
import os


def get_nltk_data_in_project():
    current_directory = os.getcwd()
    parent_directory = os.path.abspath(os.path.join(current_directory, os.pardir, os.pardir))

    nltk_data_directory = os.path.join(parent_directory, 'nltk_data')

    if not os.path.exists(nltk_data_directory):
        nltk.download('words', download_dir='C:/Users/danil/nltk_data')\

    nltk.data.path.append(nltk_data_directory)

def generate_secure_password(length, uppercase_statement=True, digits_statement=True, punctuation_statement=True):
    alphabet = ascii_lowercase

    alphabet += ascii_uppercase if uppercase_statement else ''
    alphabet += digits if digits_statement else ''
    alphabet += punctuation if punctuation_statement else ''

    password = ''.join(choice(alphabet) for _ in range(length))

    return password


def generate_mnemonic_password(password, word_length=5):
    word_list = words.words()

    mnemonic_password = ''

    for char in password:
        if char.isalpha():
            letter = char.lower()
            if letter.isalpha() and letter in 'abcdefghijklmnopqrstuvwxyz':
                word = choice([word for word in word_list if word.startswith(letter) and len(word)<= word_length])
                mnemonic_password += word if char.islower() else word.capitalize()
            else:
                mnemonic_password += char
        else:
            mnemonic_password += char

    return mnemonic_password


if __name__ == '__main__':
    get_nltk_data_in_project()

    password_length = int(input('Enter the desired password length to generate: '))

    secure_password = generate_secure_password(length=password_length)
    print(f'Your generated password {secure_password}')

    mnemonic_password = generate_mnemonic_password(secure_password)
    print(f'Your mnemonic password {mnemonic_password}')
