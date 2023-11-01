import random
import string


def generate_random_password(length):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(alphabet) for _ in range(length))
    return password


if __name__ == '__main__':
    password = generate_random_password(12)
    print(password)
